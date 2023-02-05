function clickDisplayAlert(num) {
    var question = document.getElementById('question');
    var answer = document.getElementById('answer');
    var need =[]
    switch (num){
        case 1:
            $("#answer").fadeOut(400,function(){
                $(this).html("<button onclick=\"clickDisplayAlert(11)\">5〜50万円</button> <button onclick=\"clickDisplayAlert(12)\">51万円〜100万円</button> <button onclick=\"clickDisplayAlert(13)\">101万円〜150万円</button> <button onclick=\"clickDisplayAlert(14)\">151万円〜200万円</button> <button onclick=\"clickDisplayAlert(15)\">201万円〜</button>").fadeIn(); 
            });
            $("#question").fadeOut(400,function(){
                $(this).html("<h5 class=\"font-weight-bold\">ご予算はおいくらでしょうか?</h5>").fadeIn();  
            });
            break;
        case 2:
            $("#answer").fadeOut(400,function(){
                    $(this).html("<button onclick=\"clickDisplayAlert(21)\">5〜50万円</button> <button onclick=\"clickDisplayAlert(22)\">51万円〜100万円</button> <button onclick=\"clickDisplayAlert(23)\">101万円〜150万円</button> <button onclick=\"clickDisplayAlert(24)\">151万円〜200万円</button> <button onclick=\"clickDisplayAlert(25)\">201万円〜</button>").fadeIn(); 
            });
            $("#question").fadeOut(400,function(){
                $(this).html("<h5 class=\"font-weight-bold\">ご予算はおいくらでしょうか?</h5>").fadeIn();  
            });
            break;
        case 3:
            $("#answer").fadeOut(400,function(){
                        $(this).html("<button onclick=\"clickDisplayAlert(31)\">5〜50万円</button> <button onclick=\"clickDisplayAlert(32)\">51万円〜100万円</button> <button onclick=\"clickDisplayAlert(33)\">101万円〜150万円</button> <button onclick=\"clickDisplayAlert(34)\">151万円〜200万円</button> <button onclick=\"clickDisplayAlert(35)\">201万円〜</button>").fadeIn(); 
            });
            $("#question").fadeOut(400,function(){
                $(this).html("<h5 class=\"font-weight-bold\">ご予算はおいくらでしょうか?</h5>").fadeIn();  
            });
            break;
        case 4:
            $("#answer").fadeOut(400,function(){
                        $(this).html("<button onclick=\"clickDisplayAlert(41)\">5〜50万円</button> <button onclick=\"clickDisplayAlert(42)\">51万円〜100万円</button> <button onclick=\"clickDisplayAlert(43)\">101万円〜150万円</button> <button onclick=\"clickDisplayAlert(44)\">151万円〜200万円</button> <button onclick=\"clickDisplayAlert(45)\">201万円〜</button>").fadeIn(); 
            });
            $("#question").fadeOut(400,function(){
                $(this).html("<h5 class=\"font-weight-bold\">ご予算はおいくらでしょうか?</h5>").fadeIn();  
            });
            break;
        // 5〜50万円 &軽自動車
        case 11:
            break;
        case 21:
            break;
        case 31:
            break;
        case 41:
            break;
        // 51万円〜100万円 &
        case 12:
            break;
        case 22:
            break;
        case 32:
            break;
        case 42:
            break;
        // 101万円〜150万円 &
        case 13:
            break;
        case 23:
            break;
        case 33:
            break;
        case 43:
            break;
        // 151万円〜200万円 &
        case 14:
            break;
        case 24:
            break;
        case 34:
            break;
        case 44:
            break;
        // 201万円〜 &
        case 15:
            break;
        case 25:
            break;
        case 35:
            break;
        case 45:
            break;
        default:
    }
}