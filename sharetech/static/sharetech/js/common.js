//スティッキーヘッダー
$(function(){
    $('.page_header').each(function(){
        var $window = $(window),
            $header = $(this),
            headerOffsetTop = $header.offset().top;
        $window.on('scroll', function(){
            if($window.scrollTop() > headerOffsetTop){
                $header.addClass('sticky');
            }
            else{
                $header.removeClass('sticky');
            }
        });
    });
});

//サイドメニュー
$(function(){
    var duaration = 300;
    var $navigation = $('.inner');
    var $mainNav = $navigation.find('.main_nav');
    var $menuBtn = $navigation.find('.menu_btn')
    .on('click', function(){
        $mainNav.toggleClass('open');
        if($mainNav.hasClass('open')){
            $mainNav.stop(true).animate({
                right: '-50'
            }, duaration, 'easeOutExpo');
            $menuBtn.find('.middle').stop(true).animate({
                opacity: '0'
            }, duaration, 'easeOutExpo');
            $menuBtn.find('.top').css({
                'top': '14px',
                'transform': 'rotate(45deg)'
            });
            $menuBtn.find('.bottom').css({
                'bottom': '14px',
                'transform': 'rotate(-45deg)'      
            });
        }else{
            $mainNav.stop(true).animate({
                right: '-400px'
            }, duaration, 'easeOutExpo');
            $menuBtn.find('.middle').stop(true).animate({
                opacity: '1'
            }, duaration, 'easeOutExpo');
            $menuBtn.find('.top').css({
                'top': '8px',
                'transform': 'rotate(0deg)'      
            });
            $menuBtn.find('.bottom').css({
                'bottom': '8px',
                'transform': 'rotate(0)'        
            });
        };
    });
});

// ナビゲーションメニュー open - close
$(function(){
    var $categoryContena = $('.category_contena');
    var $bigCategory = $categoryContena.find('.big_category');

    $('.big_category').on('click', function(){
        var index = $('.big_category').index(this);
        $($bigCategory[index]).find('.small_category').toggleClass('open_small_tags');
    });
});

//スムーズスクロール
$(function(){
    var btn_appear_duaration = 500
    var scroll_duaration = 500;
    var $window = $(window);
    var $backToTopBtn = $('.back_to_top');
    $window.on('scroll', $.throttle(1000/15, function(){
        if($window.scrollTop() > 0){
            $backToTopBtn.css('display', 'inline');
            $backToTopBtn.stop(true).animate({
                opacity: '1',
            }, btn_appear_duaration, 'easeOutExpo');
        }else{
            $backToTopBtn.stop(true).animate({
                opacity: '0',
            }, btn_appear_duaration, 'easeOutExpo');
            $backToTopBtn.css('display', 'none');
        }
    }));

    var el = scrollableElement('html', 'body');
    $backToTopBtn.on('click', function(event){
        event.preventDefault();
        $(el).animate({scrollTop: 0}, scroll_duaration);
    });

    function scrollableElement(){
        var i, len, $el, scrollable;
        for(i=0, len = arguments.length; i < len; i++){
            el = arguments[i],
            $el = $(el);
            if($el.scrollTop() > 0){
                return el;
            }else{
                $el.scrollTop(1);
                scrollable = $el.scrollTop() > 0;
                $el.scrollTop(0);
                if(scrollable){
                    return el;
                }
            }
        }
        return [];
    };

    $window.trigger('scroll');
});

// 記事の非同期読み込み
$(function(){
    var loadingIndex = 1;
    var isLoading = false;
    var baseURL = location.href + 'asyncLoad?page=' + document.title + '&index=';
    var $asyncLoadArticleArea = $('.async_load_article_area');
    var $window = $(window);
    var $loadingGif = $('.loading_gif');
    var $bottomArticleArea = $('.article_search');

    // 正常・エラーに関わらずajaxが完了したところで、初期状態に戻す
    $(document).on('ajaxComplete', function(){
        $loadingGif.removeClass('loading_gif is_loading');
        $loadingGif.addClass('loading_gif');
    });

    // ローディングgifが画面に配置されていれば無限ローディングの対象とする
    if($loadingGif !== null){
        $window.on('scroll', function(){
            if(($window.height() + $window.scrollTop() === $(document).height()) && !isLoading){
                isLoading = true;
                $loadingGif.addClass('loading_gif is_loading');
                // データ取得処理
                $.ajax({
                    url: baseURL + loadingIndex,
                    type: 'GET', 
                    dataType: 'html',
                    timeout: 5000,
                }).done(function(data){
                    console.log(data);
                    $asyncLoadArticleArea.append(data);
                    // エラーの場合は再度リクエストを投げないようにするため、こちらでフラグをoffにする
                    isLoading = false;
                }).fail(function(){
                    console.log('error');
                });

                loadingIndex += 1;
            }
    });
    }
});