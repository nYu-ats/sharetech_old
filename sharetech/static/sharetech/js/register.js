// 専門分野の入力欄を増減させる
$(function(){
    const $parent = $('.specialize_input_area');
    const $addBtn = $('.specialize_add_btn');
    const $baseInputArea = $parent.find('.specialize_input');
    let elementIncrementer = 1;
    const baseIdStr = $baseInputArea.find('input').attr('id');
    const maxInputAreaCount = 5;

    // 入力欄削除ボタン初期設定
    $parent.find('.specialize_delete_btn').on('click', function(){
        count = $('.specialize_input_area').find('.specialize_input').length;
        if(count > 1){
            $(this).parent().remove();
        }
    });

    // 入力欄追加
    $addBtn.on('click', function(){
        count = $('.specialize_input_area').find('.specialize_input').length;
        if(count < maxInputAreaCount){
            targetId = baseIdStr + '_' + String(elementIncrementer);
            $targetInputArea =  $($baseInputArea.clone(true));
            $targetInputArea.find('input').attr('id', targetId)
            .end()
            .find('.specialize_delete_btn')
            .on('click', function(){
                count = $('.specialize_input_area').find('.specialize_input').length;
                if(count > 1){
                    $(this).parent().remove();
                }
            })
            .end();
    
            $targetInputArea.insertBefore($addBtn);
    
            elementIncrementer++;
        }
    });
});