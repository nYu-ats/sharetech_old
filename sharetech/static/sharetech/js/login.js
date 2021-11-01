// 入力値チェック
$(function(){
    var $mailInputArea = $('.form_item input[type="email"]');
    var $mailCheckMarkImg = $($mailInputArea.siblings('img'));
    var mailValidFlg = false;
    var $passwordInputArea = $('.form_item input[type="password"]');
    var $passwordCheckMarkImg = $($passwordInputArea.siblings('img'));
    var passwordValidFlg = false;
    var $loginBtn = $('.login_button'); 

    //メールアドレスバリデーション用正規表現
    var regMail = /^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}[A-Za-z0-9_.-]{1,}\.[A-Za-z0-9]{1,}$/;
    
    // メールアドレスのバリデーション
    $mailInputArea.on('input', function(event){
        if($mailInputArea.val().match(regMail)){
            $mailCheckMarkImg.css('opacity', '1');
            mailValidFlg = true;
        }else{
            $mailCheckMarkImg.css('opacity', '0');
            mailValidFlg = false;
        }
    });

    // パスワードのバリデーション
    $passwordInputArea.on('input', function(event){
        var inputLength = $passwordInputArea.val().length;
        if(inputLength >= 8 &&  inputLength <= 30){
            $passwordCheckMarkImg.css('opacity', '1');
            passwordValidFlg = true;
        }else{
            $passwordCheckMarkImg.css('opacity', '0');
            passwordValidFlg = false;
        }
    });
});