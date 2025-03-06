export default (schema, _opts, context) => {
  if (!schema.title) {
    return [];
  }

  // Get the property name from the last element in the path
  const propertyName = context.path[context.path.length - 1];

  const normalize = (str) => str.replace(/[_ ]/g, "").toLowerCase();

  if (normalize(propertyName) === normalize(schema.title)) {
    return [
      {
        message: `Property "${propertyName}" has a title that is very similar to its name. Remove redundant title or make it more descriptive.`,
      },
    ];
  }

  return [];
};
