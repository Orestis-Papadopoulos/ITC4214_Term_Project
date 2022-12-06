
$(document).ready(function() {

    // initialize all popovers on the page
    $(function () {
        $('[data-bs-toggle="popover"]').popover()
    })

    // initialize all tooltips on the page; "popovers require the tooltip plugin as a dependency"
    $(function () {
        $('[data-bs-toggle="tooltip"]').tooltip()
    })
})
