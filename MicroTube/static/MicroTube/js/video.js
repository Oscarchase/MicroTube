function assign_params(video) {
    $('#modal-video-title').html(video.title)
    $('#modal-embedded-player').attr('src', '//www.youtube.com/embed/' + video.id)
    $('#modal-video-info').html(video.infos)
}

$(function() {
    $('#new-video-modal').on('hide.bs.modal', function () {
        $('#modal-embedded-player').attr('src', '')
    })
})
