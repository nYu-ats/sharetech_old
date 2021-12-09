// 申込処理
$(function(){
    let baseURL = location.href.replace('#', '');
    let requestURL = baseURL + '/applyCheck/';
    let $applyBtn = $('.apply_btn .button');

    const redirectURL = 'https://www.wrike.com/form/eyJhY2NvdW50SWQiOjQzMzUzNjEsInRhc2tGb3JtSWQiOjU5OTYyNn0JNDc5MTY3NzYzNjk4Ngk3NjAxZDQyZTNlMDUwNmJmNTgwMzFlMWM5ZDVhODkyNThhNmEzYjlhMWM5MjlmMGNkN2E1YWVhNWE2MWYxNDgy';

    $applyBtn.on('click', function(){
        // データ取得処理
        $.ajax({
            url: requestURL,
            type: 'GET', 
            dataType: 'json',
            timeout: 5000,
        }).done(function(data){
            if(data['result'] > 0){
                $applyBtn.text('申込中');
                $applyBtn.toggleClass('waiting');
                $applyBtn.prop('disabled', true);
                window.open(redirectURL, '_blank');
            }
        }).fail(function(){
            console.log('error');
        });
    });
});