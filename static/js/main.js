
$( document ).ready(function() {

  $('.like-form').submit(function(e){
    e.preventDefault();

    const post_id = $(this).attr('id')

    const url = $(this).attr('action')

    let res;
    const likes = $(`.like-count${post_id}`).text()

    const trim = $.trim(likes)
    var trimCount = parseInt(trim)

    const u = $('.finger')
    const i = $('.finger').attr('class')
    const clean = $.trim(i)

    $.ajax({
      type: 'POST',
      url: url,
      data: {
        'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        'post_id':post_id,
      },
      success: function(response) {
        if(clean === 'fa fa-thumbs-o-up finger') {
          $('.finger').attr('class', 'fa fa-thumbs-up finger')
          res = trimCount + 1
        }else {
          $('.finger').attr('class', 'fa fa-thumbs-o-up finger')
          res = trimCount - 1
        }
        $(`.like-count${post_id}`).text(res)
      },
      error: function(response) {
        console.log('error', response)
      }
    })
  })
});
