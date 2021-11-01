// 新着記事のスライドショー
$(function(){
    var $slideShow = $('.slides');
    var $slides = $($slideShow.find('.article'));
    var nowIndex = 0;
    var slideWidth = $($slides[0]).width();
    var referencePoint = calcSlideShowReferencePoint(slideWidth);

    setSlidesPos($slideShow, referencePoint, nowIndex);

    $(window).resize(function(){
        referencePoint = calcSlideShowReferencePoint(slideWidth);
        setSlidesPos($slideShow, referencePoint, nowIndex);
    });

    var $goToLeftBtn = $('.go_to_left');
    var $gotToRightBtn = $('.go_to_right');

    $goToLeftBtn.on('click', function(){
        $slides = $($slideShow.find('.article'));

        nowIndex -= 1;
       setSlidesPos($slideShow, referencePoint, nowIndex);
    });

    $gotToRightBtn.on('click', function(){
        $slides = $($slideShow.find('.article'));

        nowIndex += 1;
        setSlidesPos($slideShow, referencePoint, nowIndex);
    });
    

    function calcSlideShowReferencePoint(slideWidth){
        var $slideShowWrapper = $('.slide_show_block');
        return ($slideShowWrapper.width() - slideWidth) / 2;
    } 

    function calcSlidePos(index, referencePoint, slideWidth){
        return referencePoint - ((slideWidth + 32)* index);
    }
    
    function setSlidesPos($slideShowWrapper, referencePoint, index){
        var duaration = 500;

        if(index == 0){
            slidePosAdjust = calcSlidePos(index +2, referencePoint, slideWidth);
        }
        else if(index == 9){
            slidePosAdjust = calcSlidePos(index -2, referencePoint, slideWidth);
        }

        nowIndex = setSlideIndex(index, slidePosAdjust);
        setPos = calcSlidePos(nowIndex, referencePoint, slideWidth);

        $($slideShow.find('.article')).map(function(index, element){
            if(index == nowIndex){
                $(element).find('.slide_mask').removeClass('enable');
            }
            else{
                $(element).find('.slide_mask').addClass('enable');
            }
        });

        $slideShowWrapper.stop(true).animate({
            'left' : setPos
        }, duaration);
    }

    function setSlideIndex(index, slidePosAdjust){
        if(index == 0){
            $($slides[10]).remove();
            $slideShow.prepend($slides[9]).css({
                'left' : slidePosAdjust
            });
            return 1;
        }
        else if(index == 9){
            // $slides[0]をそのままappendの引数にしてもうまく要素を挿入できない
            // 一旦別変数に格納したうえでappendするとうまくいく
            insertElement = $slides[0];
            $($slides[0]).remove();
            $slideShow.append(insertElement).css({
                'left' : slidePosAdjust
            });
            return 8;
        }
        else{
            return index;
        }
    }
});