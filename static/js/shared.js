const callPostEndpoint = async (formData, endpoint) => {
  return await fetch(endpoint, {
    method: "POST",
    body: formData,
  });
};
