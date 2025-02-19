export default (schema) => {
  if (!schema.discriminator?.propertyName) {
    return [
      {
        message: "Discriminator must have a propertyName defined",
      },
    ];
  }

  const propertyName = schema.discriminator.propertyName;

  if (!schema.properties?.[propertyName]) {
    return [
      {
        message: `The discriminator property "${propertyName}" must exist in the schema properties`,
      },
    ];
  }
};
