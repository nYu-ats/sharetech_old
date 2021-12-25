$(function(){
    let $formItem = $('.form_container form');
    let $openDeleteBtn = $('.delete_btn');
    let $deleteConfirm = $formItem.find('.delete_overlay');
    let $closeDeleteBtn = $formItem.find('.delete_overlay .delete_confirm .flex p');
    let $deleteBtn = $formItem.find('.delete_overlay .delete_confirm .flex input');
    let $deleteFlg = $formItem.find('.delete_overlay .delete_confirm .delete_flg');


    // 削除実行時に既存の窓口内容の差分を無くすため初期状態を保存
    let titleTxt = $formItem.find('.title input').val();
    let overviewTxt = $formItem.find('.overview textarea').val();
    let archivementTxt = $formItem.find('.archivement textarea').val();
    let price = $formItem.find('.price input').val();
    let url = $formItem.find('.url input').val();

    // 削除確認パネルオープン
    $openDeleteBtn.on('click', function(){
        $deleteConfirm.toggleClass('hidden');
        $deleteFlg.prop('checked', true);
    }) ;

    // 削除確認パネルクローズ
    $closeDeleteBtn.on('click', function(){
        $deleteConfirm.toggleClass('hidden');
        $deleteFlg.prop('checked', true);
    });

    // 削除POST時に既存データの再セット
    $deleteBtn.submit(function(){
        $formItem.find('.title input').val(titleTxt);
        $formItem.find('.overview textarea').val(overviewTxt);
        $formItem.find('.archivement textarea').val(archivementTxt);
        $formItem.find('.price input').val(price);
        $formItem.find('.url input').val(url);

    });
});