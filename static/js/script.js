document.addEventListener('DOMContentLoaded', function() {
    
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // select initialisation
    select = document.querySelectorAll('select');
    M.FormSelect.init(select);

});