setTimeout(() => {
  var deleteForms = document.getElementsByClassName("delete-form");
  deleteForms.forEach((form) => {
    form.addEventListener('click', () => {
      if(confirm('Are you sure you want to delete?')) {
        form.submit();
      }
    });
  });
}, 1);