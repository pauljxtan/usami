// Get

function getTotals() {
  $.get('/totals/', {}, gotTotals);
}

function gotTotals(data) {
  loadTotals(data);
}

// Load

function loadTotals(data) {
  var totals = JSON.parse(data);

  doSomethingWithFade('#total-nouns', function() { $('#total-nouns').html(totals.total_nouns); }, doNothing);
  doSomethingWithFade('#total-verbs', function() { $('#total-verbs').html(totals.total_verbs); }, doNothing);
  doSomethingWithFade('#total-adjectives', function() { $('#total-adjectives').html(totals.total_adjectives); }, doNothing);
  doSomethingWithFade('#total-adverbs', function() { $('#total-adverbs').html(totals.total_adverbs); }, doNothing);
  doSomethingWithFade('#total-miscs', function() { $('#total-miscs').html(totals.total_miscs); }, doNothing);

  doSomethingWithFade('#total-nouns-archived', function() { $('#total-nouns-archived').html(totals.total_nouns_archived); }, doNothing);
  doSomethingWithFade('#total-verbs-archived', function() { $('#total-verbs-archived').html(totals.total_verbs_archived); }, doNothing);
  doSomethingWithFade('#total-adjectives-archived', function() { $('#total-adjectives-archived').html(totals.total_adjectives_archived); }, doNothing);
  doSomethingWithFade('#total-adverbs-archived', function() { $('#total-adverbs-archived').html(totals.total_adverbs_archived); }, doNothing);
  doSomethingWithFade('#total-miscs-archived', function() { $('#total-miscs-archived').html(totals.total_miscs_archived); }, doNothing);
}

function loadNouns() {
  $.get('/jp/nouns/rows/', {}, gotRows);
  $('#div-nouns-modals').load('/jp/nouns/modals/');
}

function loadMessage(data) {
  var message = JSON.parse(data).message;
  console.log(message);
  console.log(message.level);
  console.log(message.text);
  doSomethingWithFade('#div-message', function() {
    $('#div-message').attr('class', 'alert alert-' + message.level);
    $('#span-message').html(message.text);
  }, doNothing);
}

function gotRows(data) {
  doSomethingWithFade('#table-nouns', function() {
    $('#table-nouns').bootstrapTable('load', JSON.parse(data));
  }, doNothing);
}

// Modify data

function addNoun() {
  $.post('/jp/noun/add/', {
        vocab: $('#input-noun-add-vocab').val(),
        phonetic: $('#input-noun-add-phonetic').val(),
        english: $('#input-noun-add-english').val(),
        category: $('#input-noun-add-category').val()
      },
      addedNoun);
}

function addedNoun(data) {
  loadMessageAndRefreshNouns(data);
}

function deleteNoun(id) {
  // TODO: Get confirmation
  $.post('/noun/delete/'+id+'/', {}, deletedNoun);
}

function deletedNoun(data) {
  loadMessageAndRefreshNouns(data);
}

function archiveNoun(id) {
  // TODO: Get confirmation
  $.post('/noun/archive/'+id+'/', {}, archivedNoun);
}

function archivedNoun(data) {
  loadMessageAndRefreshNouns(data);
}

function loadMessageAndRefreshNouns(data) {
  loadMessage(data);
  getTotals();
  loadNouns();
}

// Extensions

function loadBootstrapTable(tableId) {
  doSomethingWithFade(tableId, function() {
    $(tableId).bootstrapTable()
  }, doNothing);
}

function vocabCellStyle(value, row, index) {
  return {
    classes: 'vocab-vocab'
  };
}

// Effects

function doSomethingWithFade(elementIdToFade, doSomething, callback) {
  $(elementIdToFade).fadeOut(function() {
    doSomething();
    $(elementIdToFade).fadeIn(callback);
  });
}

// Misc

function doNothing() {}