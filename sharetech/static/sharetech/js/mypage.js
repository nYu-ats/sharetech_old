// 申込・作成相談窓口の切り替え処理
$(function(){
    let $displaySwitchBtn = $('.switch_tab div');
    let $displayArea = $('.consutl_windodw_flex');
    let $consultWindowAll = $displayArea.find('.article');

    // 相談窓口の一覧を申込・作成に切り分ける
    let applyConsultWindowList = [];
    let createConsultWindowList = [];

    $consultWindowAll.each(function(index, element){
        if($(element).attr('control_flg') === '0'){
            applyConsultWindowList.push(element);
        }else{
            createConsultWindowList.push(element);
        }
    });

    // 初期化処理
    // 初回アクセス時は申込相談窓口を表示する
    let disaplyFlg = '0';

    // 初期表示
    $displayArea.empty();
    if(disaplyFlg === '0'){
        $displayArea.append(applyConsultWindowList);
    }else{
        $displayArea.append(createConsultWindowList);
    }

    // 切り替えイベント設定
    $displaySwitchBtn.each(function(index, element){
        $(element).on('click', function(){
            controlFlg = $(this).attr('control_flg');

            // 表示相談窓口切り替え
            if(controlFlg !== disaplyFlg){
                $displayArea.empty();
                if(controlFlg === '0'){
                    $displayArea.append(applyConsultWindowList);
                }else{
                    $displayArea.append(createConsultWindowList);
                }
                
                // ボタンセレクタ切り替え
                $displaySwitchBtn.each(function(index, element){
                    $(element).removeClass('active');
                });
                $(this).addClass('active');

                disaplyFlg = controlFlg;
            }
        });        
    });    
});