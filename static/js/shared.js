const getLoadSpinner = () =>
  '<div class="mdl-spinner mdl-spinner--single-color mdl-js-spinner is-active" id="loadingSpinner"></div>';

const callPostEndpoint = async (formData, endpoint) => {
  return await fetch(endpoint, {
    method: "POST",
    body: formData,
  });
};
