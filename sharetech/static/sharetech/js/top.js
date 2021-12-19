// 記事の非同期読み込み
$(function(){
    let loadingIndex = 1;
    let isLoading = false;
    let baseURL = location.href + 'asyncLoad?page=' + document.title + '&index=';
    // URLに#(自ページへのリンク)が含まれる可能性があるためトリミング
    baseURL = baseURL.replace('#', '');

    let $asyncLoadArticleArea = $('.async_load_article_area');
    let $window = $(window);
    let $loadingGif = $('.loading_gif');
    let isTarget = true; 
    // 非同期ローディング対象判定
    if($asyncLoadArticleArea.size() == 0){
        isTarget = false;
    }

    // 正常・エラーに関わらずajaxが完了したところで、初期状態に戻す
    $(document).on('ajaxComplete', function(){
        $loadingGif.removeClass('loading_gif is_loading');
        $loadingGif.addClass('loading_gif');
    });

    // ローディングgifが画面に配置されていれば無限ローディングの対象とする
    if(isTarget && $loadingGif !== null){
        $window.on('scroll', function(){
            if(($window.height() + $window.scrollTop() === $(document).height()) && !isLoading){
                isLoading = true;
                $loadingGif.addClass('loading_gif is_loading');
                getUrl = baseURL + String(loadingIndex);
                // データ取得処理
                $.ajax({
                    url: getUrl,
                    type: 'GET', 
                    dataType: 'html',
                    timeout: 5000,
                }).done(function(data){
                    $asyncLoadArticleArea.append(data);
                    // エラーの場合は再度リクエストを投げないようにするため、こちらでフラグをoffにする
                    isLoading = false;
                    loadingIndex += 1;
                }).fail(function(){
                    console.log('load error');
                });
            }
    });
    }
});
