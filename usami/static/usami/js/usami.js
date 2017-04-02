function initPage() {
  getTotals();
  loadNouns();
  loadVerbs();
  loadAdjectives();
  loadAdverbs();
  loadMiscs();
}

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
  $.get('/jp/nouns/rows/', {}, loadedNouns);
  $('#div-nouns-modals').load('/jp/nouns/modals/');
  $('#table-category-counts-nouns-tbody').load('/jp/nouns/catcounts/');
}

function loadedNouns(data) {
  doSomethingWithFade('#table-nouns', function() {
    $('#table-nouns').bootstrapTable('load', JSON.parse(data));
  }, doNothing);
}

function loadVerbs() {
  $.get('/jp/verbs/rows/', {}, loadedVerbs);
  $('#div-verbs-modals').load('/jp/verbs/modals/');
  $('#table-category-counts-verbs-tbody').load('/jp/verbs/catcounts/');
}

function loadedVerbs(data) {
  doSomethingWithFade('#table-verbs', function() {
    $('#table-verbs').bootstrapTable('load', JSON.parse(data));
  }, doNothing);
}

function loadAdjectives() {
  $.get('/jp/adjectives/rows/', {}, loadedAdjectives);
  $('#div-adjectives-modals').load('/jp/adjectives/modals/');
  $('#table-category-counts-adjectives-tbody').load('/jp/adjectives/catcounts/');
}

function loadedAdjectives(data) {
  doSomethingWithFade('#table-adjectives', function() {
    $('#table-adjectives').bootstrapTable('load', JSON.parse(data));
  }, doNothing);
}

function loadAdverbs() {
  $.get('/jp/adverbs/rows/', {}, loadedAdverbs);
  $('#div-adverbs-modals').load('/jp/adverbs/modals/');
  $('#table-category-counts-adverbs-tbody').load('/jp/adverbs/catcounts/');
}

function loadedAdverbs(data) {
  doSomethingWithFade('#table-adverbs', function() {
    $('#table-adverbs').bootstrapTable('load', JSON.parse(data));
  }, doNothing);
}

function loadMiscs() {
  $.get('/jp/miscs/rows/', {}, loadedMiscs);
  $('#div-miscs-modals').load('/jp/miscs/modals/');
  $('#table-category-counts-miscs-tbody').load('/jp/miscs/catcounts/');
}

function loadedMiscs(data) {
  doSomethingWithFade('#table-miscs', function() {
    $('#table-miscs').bootstrapTable('load', JSON.parse(data));
  }, doNothing);
}

function loadMessage(data) {
  var message = JSON.parse(data).message;
  doSomethingWithFade('#div-message', function() {
    $('#div-message').attr('class', 'alert alert-' + message.level);
    $('#span-message').html(message.text);
  }, doNothing);
}

// Add

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

function addVerb() {
  $.post('/jp/verb/add/', {
        vocab: $('#input-verb-add-vocab').val(),
        phonetic: $('#input-verb-add-phonetic').val(),
        english: $('#input-verb-add-english').val(),
        category: $('#input-verb-add-category').val(),
        transitivity: $('#select-verb-add-transitivity').val(),
        jp_type: $('#select-verb-add-jp-type').val()
      },
      addedVerb);
}

function addedVerb(data) {
  loadMessageAndRefreshVerbs(data);
}

function addAdjective() {
  $.post('/jp/adjective/add/', {
        vocab: $('#input-adjective-add-vocab').val(),
        phonetic: $('#input-adjective-add-phonetic').val(),
        english: $('#input-adjective-add-english').val(),
        category: $('#input-adjective-add-category').val(),
        jp_type: $('#select-adjective-add-jp-type').val()
      },
      addedAdjective);
}

function addedAdjective(data) {
  loadMessageAndRefreshAdjectives(data);
}

function addAdverb() {
  $.post('/jp/adverb/add/', {
        vocab: $('#input-adverb-add-vocab').val(),
        phonetic: $('#input-adverb-add-phonetic').val(),
        english: $('#input-adverb-add-english').val(),
        category: $('#input-adverb-add-category').val()
      },
      addedAdverb);
}

function addedAdverb(data) {
  loadMessageAndRefreshAdverbs(data);
}

function addMisc() {
  $.post('/jp/misc/add/', {
        vocab: $('#input-misc-add-vocab').val(),
        phonetic: $('#input-misc-add-phonetic').val(),
        english: $('#input-misc-add-english').val(),
        category: $('#input-misc-add-category').val()
      },
      addedMisc);
}

function addedMisc(data) {
  loadMessageAndRefreshMiscs(data);
}

// Edit

function editNoun(id) {
  console.log($('#input-noun-edit-vocab-'+id).val());
  console.log($('#input-noun-edit-phonetic-'+id).val());
  console.log($('#input-noun-edit-english-'+id).val());
  console.log($('#input-noun-edit-category-'+id).val());
  $.post('/noun/edit/'+id+'/', {
        vocab: $('#input-noun-edit-vocab-'+id).val(),
        phonetic: $('#input-noun-edit-phonetic-'+id).val(),
        english: $('#input-noun-edit-english-'+id).val(),
        category: $('#input-noun-edit-category-'+id).val()
      },
      editedNoun);
}

function editedNoun(data) {
  loadMessageAndRefreshNouns(data);
}

// Delete

function deleteNoun(id) {
  // TODO: Get confirmation
  $.post('/noun/delete/'+id+'/', {}, deletedNoun);
}

function deletedNoun(data) {
  loadMessageAndRefreshNouns(data);
}

function deleteVerb(id) {
  $.post('/verb/delete/'+id+'/', {}, deletedVerb);
}

function deletedVerb(data) {
  loadMessageAndRefreshVerbs(data);
}

function deleteAdjective(id) {
  $.post('/adjective/delete/'+id+'/', {}, deletedAdjective);
}

function deletedAdjective(data) {
  loadMessageAndRefreshAdjectives(data);
}

function deleteAdverb(id) {
  $.post('/adverb/delete/'+id+'/', {}, deletedAdverb);
}

function deletedAdverb(data) {
  loadMessageAndRefreshAdverbs(data);
}

function deleteMisc(id) {
  $.post('/misc/delete/'+id+'/', {}, deletedMisc);
}

function deletedMisc(data) {
  loadMessageAndRefreshMiscs(data);
}

// Archive

function archiveNoun(id) {
  // TODO: Get confirmation
  $.post('/noun/archive/'+id+'/', {}, archivedNoun);
}

function archivedNoun(data) {
  loadMessageAndRefreshNouns(data);
}

function archiveVerb(id) {
  $.post('/verb/archive/'+id+'/', {}, archivedVerb);
}

function archivedVerb(data) {
  loadMessageAndRefreshVerbs(data);
}

function archiveAdjective(id) {
  $.post('/adjective/archive/'+id+'/', {}, archivedAdjective);
}

function archivedAdjective(data) {
  loadMessageAndRefreshAdjectives(data);
}

function archiveAdverb(id) {
  $.post('/adverb/archive/'+id+'/', {}, archivedAdverb);
}

function archivedAdverb(data) {
  loadMessageAndRefreshAdverbs(data);
}

function archiveMisc(id) {
  $.post('/misc/archive/'+id+'/', {}, archivedMisc);
}

function archivedMisc(data) {
  loadMessageAndRefreshMiscs(data);
}

// Refresh

function loadMessageAndRefreshNouns(data) {
  loadMessage(data);
  getTotals();
  loadNouns();
}

function loadMessageAndRefreshVerbs(data) {
  loadMessage(data);
  getTotals();
  loadVerbs();
}

function loadMessageAndRefreshAdjectives(data) {
  loadMessage(data);
  getTotals();
  loadAdjectives();
}

function loadMessageAndRefreshAdverbs(data) {
  loadMessage(data);
  getTotals();
  loadAdverbs();
}

function loadMessageAndRefreshMiscs(data) {
  loadMessage(data);
  getTotals();
  loadMiscs();
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