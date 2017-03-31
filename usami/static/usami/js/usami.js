// AJAX calls

function getAllNouns() {
  $.get('/jp/nouns/all/', {}, gotAllNouns, 'json');
}

// function getNounsTab() {
//   $.get('/jp/nouns/tab/', {}, gotNounsTab, 'html');
// }

function getNounsTab() {
  $('#table-nouns-tbody').load('/jp/nouns/tab/');
}

// Callbacks

function gotAllNouns(data) {
  console.log("Got all nouns");
  loadNounVocabs(data);
  console.log("Loaded noun vocabs")
}

function gotNounsTab(data) {
  console.log("Got noun tab");
  loadNounsTab(data);
  console.log("Loaded noun tab");
}

// Loaders

function loadNounVocabs(data) {
  html = '';
  // for (var i = 0; i < data.length; i++) {
  //   var noun = data[i][0];
  //   ruby = data[i][1];
  //   var id = noun['id'];
  //   var vocab = noun['vocab'];
  //   var english = noun['english'];
  //   var category = noun['category'];
  //   html += '<tr class="vocab-row">';
  //   html += '  <td class="vocab vocab-vocab">'+ruby+'</td>';
  //   html += '  <td class="vocab vocab-english">'+english+'</td>';
  //   html += '  <td class="vocab vocab-category">'+category+'</td>';
  //   html += '  <td class="vocab vocab-buttons">';
  //   html += '    <a class="btn btn-primary" data-toggle="modal" data-target="#noun-form-'+id+'">Edit</a>';
  //   html += '    <a class="btn btn-danger" href="/noun/delete/'+id+'/">Delete</a>';
  //   html += '    <a class="btn btn-success" href="/noun/archive/'+id+'/">Archive</a>';
  //   html += '  </td>';
  //   html += '</tr>';
  //   html += '<div class="modal fade" id="noun-form-'+id+'" tabindex="-1" role="dialog" aria-labelledby="noun-form-label-'+id+'{{ noun.0.id }}">';
  //   html += '  <div class="modal-dialog" role="document">';
  //   html += '    <div class="modal-content">';
  //   html += '      <div class="modal-header">';
  //   html += '        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>';
  //   html += '        <h4 class="modal-title" id="noun-form-label-'+id+'{{ noun.0.id }}">Edit '+ruby+'</h4>';
  //   html += '      </div>';
  //   html += '      <div class="modal-body">';
  //   html += '        <form class="form-inline" action="noun/edit/'+id+'/" method="post">';
  //   html += '          <div class="form-group">';
  //   html += '            <label for="id_vocab">Vocab:</label>';
  //   html += '            <input class="form-control" id="id_vocab" maxlength="16" name="vocab" type="text" required="" value="'+vocab+'">';

    //     </div>
    //     <div class="form-group">
    //     <label for="id_phonetic">Phonetic:</label>
    // <input class="form-control" id="id_phonetic" maxlength="32" name="phonetic" type="text" required=""
    // value="{{ noun.0.phonetic }}">
    //     </div>
    //     <div class="form-group">
    //     <label for="id_english">English:</label>
    // <input class="form-control" id="id_english" maxlength="32" name="english" type="text" required=""
    // value="{{ noun.0.english }}">
    //     </div>
    //     <div class="form-group">
    //     <label for="id_category">Category:</label>
    // <input class="form-control" id="id_category" maxlength="32" name="category" type="text" required=""
    // value="{{ noun.0.category }}">
    //     </div>
    //     <div class="modal-footer">
    //     <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
    //     <button type="submit" class="btn btn-primary">Save changes</button>
    // </div>
    // </form>
    // </div>
    // </div>
    // </div>
    // </div>
  // }
  //$('#table-nouns-tbody').html(html);
}

function loadNounsTab(data) {
  $('#table-nouns-tbody').html(data);
}