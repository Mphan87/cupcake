// $('.delete-cupcake').click(function() {
// const id = $(this).data('id')
// // .data is a special method in jquerry to get a data-id
// alert(id)

// })

$('.delete-cupcake').click(deleteCupcake)
async function deleteCupcake() {
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove
}


function generateCupcakeHTML(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
          <button class="delete-button">X</button>
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)">
      </div>
    `;
  }

//   async function showInitialCupcakes() {
//     const response = await axios.get(`${BASE_URL}/cupcakes`);
  
//     for (let cupcakeData of response.data.cupcakes) {
//       let newCupcake = $(generateCupcakeHTML(cupcakeData));
//       $("#cupcakes-list").append(newCupcake);
//     }
//   }
  
  $("#new-cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();
  
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();
  
    const newCupcakeResponse = await axios.post(`/api/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });
  
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
  });
  
  