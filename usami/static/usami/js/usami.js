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
  doSomethingWithFade('#total-nouns', function() { $('#total-nouns').html(totals['total_nouns']); }, doNothing);
  doSomethingWithFade('#total-verbs', function() { $('#total-verbs').html(totals['total_verbs']); }, doNothing);
  doSomethingWithFade('#total-adjectives', function() { $('#total-adjectives').html(totals['total_adjectives']); }, doNothing);
  doSomethingWithFade('#total-adverbs', function() { $('#total-adverbs').html(totals['total_adverbs']); }, doNothing);
  doSomethingWithFade('#total-miscs', function() { $('#total-miscs').html(totals['total_miscs']); }, doNothing);
}

function loadNouns() {
  //doSomethingWithFade('#table-nouns-tbody', function() { $('#table-nouns-tbody').load('/jp/nouns/tbody/') }, loadedNouns);
  loadedNouns();
  $('#div-nouns-modals').load('/jp/nouns/modals/');
}

function loadedNouns() {
  //loadBootstrapTable('#table-nouns');

  $.get('/jp/nouns/rows/', {}, gotRows);
}

function gotRows(data) {
  $('#table-nouns').bootstrapTable('load', JSON.parse(data));
}


// Modify data

function addNoun() {
  $.post('/jp/noun/add/', {
        'vocab': $('#input-noun-add-vocab').val(),
        'phonetic': $('#input-noun-add-phonetic').val(),
        'english': $('#input-noun-add-english').val(),
        'category': $('#input-noun-add-category').val()
      },
      addedNoun);
}

function addedNoun(data) {
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