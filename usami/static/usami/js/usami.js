// AJAX calls
function getAllNouns() {
  $.get('/jp/nouns/all/', {}, gotAllNouns, 'json');
}

// Callbacks
function gotAllNouns(data) {
  console.log("Got all nouns");
  loadNounVocabs(data);
  console.log("Loaded noun vocabs")
}

// Loaders
function loadNounVocabs(data) {
  html = '';
  for (var i = 0; i < data.length; i++) {
    var noun = data[i][0];
    ruby = data[i][1];
    var id = noun['id'];
    var english = noun['english'];
    var category = noun['category'];
    html += '<tr class="vocab-row">';
    html += '  <td class="vocab vocab-vocab">'+ruby+'</td>';
    html += '  <td class="vocab vocab-english">'+english+'</td>';
    html += '  <td class="vocab vocab-category">'+category+'</td>';
    html += '  <td class="vocab vocab-buttons">';
    html += '    <a class="btn btn-primary" data-toggle="modal" data-target="#noun-form-'+id+'">Edit</a>';
    html += '    <a class="btn btn-danger" href="/noun/delete/'+id+'/">Delete</a>';
    html += '    <a class="btn btn-success" href="/noun/archive/'+id+'/">Archive</a>';
    html += '  </td>';
    html += '</tr>';
  }
  //$('#table-nouns-tbody').html(html);
  // {#                <div class="modal fade" id="noun-form-{{ noun.0.id }}" tabindex="-1" role="dialog"#}
  // {#                     aria-labelledby="noun-form-label-{{ noun.0.id }}">#}
  // {#                  <div class="modal-dialog" role="document">#}
  // {#                    <div class="modal-content">#}
  // {#                      <div class="modal-header">#}
  // {#                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>#}
  // {#                        <h4 class="modal-title" id="noun-form-label-{{ noun.0.id }}">Edit {{ noun.1 | safe }}</h4>#}
  // {#                      </div>#}
  // {#                      <div class="modal-body">#}
  // {#                        <form class="form-inline" action="{% url 'edit_noun' noun.0.id %}" method="post">#}
  // {#                          {% csrf_token %}#}
  // {#                          <div class="form-group">#}
  // {#                            <label for="id_vocab">Vocab:</label>#}
  // {#                            <input class="form-control" id="id_vocab" maxlength="16" name="vocab" type="text" required=""#}
  // {#                                   value="{{ noun.0.vocab }}">#}
  // {#                          </div>#}
  // {#                          <div class="form-group">#}
  // {#                            <label for="id_phonetic">Phonetic:</label>#}
  // {#                            <input class="form-control" id="id_phonetic" maxlength="32" name="phonetic" type="text" required=""#}
  // {#                                   value="{{ noun.0.phonetic }}">#}
  // {#                          </div>#}
  // {#                          <div class="form-group">#}
  // {#                            <label for="id_english">English:</label>#}
  // {#                            <input class="form-control" id="id_english" maxlength="32" name="english" type="text" required=""#}
  // {#                                   value="{{ noun.0.english }}">#}
  // {#                          </div>#}
  // {#                          <div class="form-group">#}
  // {#                            <label for="id_category">Category:</label>#}
  // {#                            <input class="form-control" id="id_category" maxlength="32" name="category" type="text" required=""#}
  // {#                                   value="{{ noun.0.category }}">#}
  // {#                          </div>#}
  // {#                          <div class="modal-footer">#}
  // {#                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>#}
  // {#                            <button type="submit" class="btn btn-primary">Save changes</button>#}
  // {#                          </div>#}
  // {#                        </form>#}
  // {#                      </div>#}
  // {#                    </div>#}
  // {#                  </div>#}
  // {#                </div>#}
  // {##}
  // {#              {% endfor %}#}
}