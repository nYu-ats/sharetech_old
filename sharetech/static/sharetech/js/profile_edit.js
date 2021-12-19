// 不要な要素の削除
// djangoフォームにて不要なリンク、テキストが挿入されるため
$(function(){
    let $targetArea = $('.icon_image');
    let $label = $targetArea.find('label');
    let $input = $targetArea.find('input');
    let $canvas = $targetArea.find('.image_container');
    $targetArea.empty();
    $targetArea.append($label);
    $targetArea.append($input);
    $targetArea.append($canvas);
});

// アップロードされた画像のプレビュー表示
$(function(){
    let $fileField = $('.icon_image');
    let $inputArea = $fileField.find('input');
    let $previewArea = $fileField.find('canvas');
    let file = null;
    let blob = null;
    
    
    $inputArea.change(function(){
        
        // アップロードファイルの画像判定
        file = $(this).prop('files')[0];
        if (file.type != 'image/jpeg' && file.type != 'image/png'){
            file = null;
            blob = null;
            return 
        }
        
        let reader = new FileReader();
        let targetImage = new Image();
        reader.onload = function(e){
            targetImage.onload = function(){
                // プレビュー描画
                let imageSize = ResizeImage(targetImage);
                
                $previewArea.attr('width', imageSize.width).attr('height', imageSize.height);
                let context = $previewArea[0].getContext('2d');
                context.clearRect(0, 0, imageSize.width, imageSize.height);
                context.drawImage(
                    targetImage,0,0,targetImage.width,targetImage.height,0,0,imageSize.width,imageSize.height
                    );

                // アップロード用のリサイズ画像生成
                let base64 = $previewArea.get(0).toDataURL(file.type);
                let bin = atob(base64.split('base64,')[1]);
                let len = bin.length;
                let barr = new Uint8Array(len);
                let index = 0;

                while(index < len){
                    barr[index] = bin.charCodeAt(index);
                    index++;
                }

                resizedBlob = new Blob([barr], {type: file.type});
                file.blob = resizedBlob;
                file.size = resizedBlob.size;
                console.log("==========after trimming=====================")
                console.log("resizedBlob.size")
                console.log(resizedBlob.size)
                console.log("resizedBlob")
                console.log(resizedBlob)
                console.log("file")
                console.log(file)
            }
            targetImage.src = e.target.result;
        }
        console.log("==========before trimming=====================")
        console.log(file)
        reader.readAsDataURL(file);
    });

    // 画像リサイズ
    // 【to be】cropperで置き換え
    function ResizeImage(image){
        const baseSize = 175;
        targetImgHeight = image.height;
        targetImgWidth = image.width;
    
        if(targetImgHeight > targetImgWidth){
            resizeWidth = baseSize;
            resizeHeight = targetImgHeight * baseSize / targetImgWidth;
        }else{
            resizeHeight = baseSize;
            resizeWidth = targetImgWidth * baseSize / targetImgHeight;
        }
    
        return {'width': resizeWidth, 'height': resizeHeight};
    }
});