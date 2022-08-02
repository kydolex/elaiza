$(function() {
  $('textarea').atwho({
    at: '<pre',
    data: [
      {name: 'java', content: '<pre><code class="java">\n</code></pre>'},
      {name: 'sql', content: '<pre><code class="sql">\n</code></pre>'}],
    insertTpl: '${content}',
    suffix: ''
  }).atwho({
    at: 'template',
    data: [
      {name: 'バグ', content: 'h2. 発生バージョン\n\nh2. 再現手順\n\nh2. ログ\n\n'},
      {name: '問い合わせ', content: 'h2. 問い合わせ内容\n\nh2. 回答期限\n\n'}],
    insertTpl: '${content}',
    suffix: ''
  })
  // .atwho({
  //   at: 'h',
  //   data: [
  //     {name: 'h1', content: '<h1></h1>'},
  //     {name: 'h2', content: '<h2></h2>'},
  //     {name: 'h3', content: '<h3></h3>'},
  //     {name: 'h4', content: '<h4></h4>'},
  //     {name: 'h5', content: '<h5></h5>'},
  //     {name: 'h6', content: '<h6></h6>'}],
  //   insertTpl: '${content}',
  //   suffix: ''
  // })
  ;
});


window.addEventListener('DOMContentLoaded', function () {
  const input_element = document.getElementById('liveeditor');
  input_element.addEventListener('input', function (e) {
    function getCaret(el) { 
      if (el.selectionStart) { 
        return el.selectionStart; 
      } else if (document.selection) { 
        el.focus(); 
    
        var r = document.selection.createRange(); 
        if (r == null) { 
          return 0; 
        } 
    
        var re = el.createTextRange(), 
            rc = re.duplicate(); 
        re.moveToBookmark(r.getBookmark()); 
        rc.setEndPoint('EndToStart', re); 
    
        return rc.text.length; 
      }  
      return 0; 
    }
    var text = input_element.value.substring(0, getCaret(input_element));
    switch (text.slice(-4)) {
      case "<h1>":complete_quote(input_element, '</h1>');break;
      case "<h2>":complete_quote(input_element, '</h2>');break;
      case "<h3>":complete_quote(input_element, '</h3>');break;
      case "<h4>":complete_quote(input_element, '</h4>');break;
      case "<h5>":complete_quote(input_element, '</h5>');break;
      case "<h6>":complete_quote(input_element, '</h6>');break;
      case "<li>":complete_quote(input_element, '</li>');break;
      case "<ul>":complete_quote(input_element, '</ul>');break;
      case "<ol>":complete_quote(input_element, '</ol>');break;
      case "<dl>":complete_quote(input_element, '</dl>');break;
      case "<dd>":complete_quote(input_element, '</dd>');break;
      case "<tr>":complete_quote(input_element, '</tr>');break;
      case "<td>":complete_quote(input_element, '</td>');break;
      case "<th>":complete_quote(input_element, '</th>');break;
      case "<em>":complete_quote(input_element, '</em>');break;
    }
    switch (text.slice(-5)) {
      case "<div>":complete_quote(input_element, '</div>');break;
      case "<del>":complete_quote(input_element, '</del>');break;
      case "<dfn>":complete_quote(input_element, '</dfn>');break;
      case "<sup>":complete_quote(input_element, '</sup>');break;
      case "<sub>":complete_quote(input_element, '</sub>');break;
      case "<pre>":complete_quote(input_element, '</pre>');break;
      case "<var>":complete_quote(input_element, '</var>');break;
      case "<kbd>":complete_quote(input_element, '</kbd>');break;
      case "<big>":complete_quote(input_element, '</big>');break;
    }
  });
  //後ろに補完する関数
  function complete_quote(element, charactor) {
    const content = element.value;
    const len = content.length;
    const pos = element.selectionStart;
    element.value = content.substr(0, pos) + charactor + content.substr(pos, len);
    element.setSelectionRange(pos, pos);
  }
  //そっくり入れ替える関数
  function replace_quote(element, charactor) {
    const content = element.value;
    const len = content.length;
    const pos = element.selectionStart;
    element.value = content.substr(0, pos - 1) + charactor + content.substr(pos, len);
    element.setSelectionRange(pos, pos);
  }
});
