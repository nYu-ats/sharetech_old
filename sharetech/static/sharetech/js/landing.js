var scrollAnimationElm = document.querySelectorAll('.sa');
var scrollAnimationFunc = function() {
  for(var i = 0; i < scrollAnimationElm.length; i++) {
    var triggerMargin = 300;
    if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
      scrollAnimationElm[i].classList.add('show');
    }
  }
}
window.addEventListener('load', scrollAnimationFunc);
window.addEventListener('scroll', scrollAnimationFunc);

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
