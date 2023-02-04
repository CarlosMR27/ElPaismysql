function confirmarEliminacion(id){
    Swal.fire({
        title: 'Estás seguro?',
        text: "No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Bórralo!'
      }).then((result) => {
        if (result.isConfirmed) {
            //Elimina el comentario
            window.location.href="/eliminar_comentario/"+id+"/"
          Swal.fire(
            "Eliminando comentario..."
          )
        }
        location.reload()
      })
}