const csrftoken = Cookies.get('csrftoken');

let deleteButtons = document.querySelectorAll('.delete_alert');
console.log(deleteButtons)

for (let deleteButton of deleteButtons){
  deleteButton.addEventListener('click', function(e){
  alert('Are you sure you want to delete?');

// request that tells JS to 'fetch' but then stay on the page
  let albumId = e.target.dataset.album
  fetch(`/albums/${albumId}/delete/`, {
      method:'POST',
      headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    "X-Requested-With": "XMLHttpRequest",
    "X-CSRFToken": csrftoken
  },
    credentials: 'include'
    }).then(response => response.json())
    .then(data => {
      console.log(data);
      // remove whole div after the delete
      e.target.parentNode.parentNode.parentNode.remove();
    }) 


})
}





