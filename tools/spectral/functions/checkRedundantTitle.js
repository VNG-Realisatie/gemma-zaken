export default (schema, _opts, context) => {
  const normalize = (str) => str.replace(/[_ ]/g, "").toLowerCase();

  // Case 1: Property name matches title
  if (schema.title && context.path.includes("properties")) {
    const propertyName = context.path[context.path.length - 1];

    if (normalize(propertyName) === normalize(schema.title)) {
      return [
        {
          message: `Property "${propertyName}" has a title that is very similar to its name. Remove redundant title or make it more descriptive.`,
        },
      ];
    }
  }

  // Case 2: Parameter name matches schema title
  if (schema.name && schema.schema && schema.schema.title) {
    if (normalize(schema.name) === normalize(schema.schema.title)) {
      return [
        {
          message: `Parameter "${schema.name}" has a schema title that is very similar to its name. Remove redundant title or make it more descriptive.`,
        },
      ];
    }
  }

  // Case 3: Schema name in components matches title
  if (schema.title && context.path.includes("schemas")) {
    const schemaName = context.path[context.path.length - 1];

    if (normalize(schemaName) === normalize(schema.title)) {
      return [
        {
          message: `Schema "${schemaName}" has a title that is very similar to its name. Remove redundant title or make it more descriptive.`,
        },
      ];
    }
  }

  // Case 4: Array item titles match the parent schema name
  if (schema.title && context.path.includes("items")) {
    // Get the parent schema name (two levels up from items)
    const parentSchemaName = context.path[context.path.length - 2];

    if (normalize(parentSchemaName) === normalize(schema.title)) {
      return [
        {
          message: `Array item title "${schema.title}" is redundant with its parent schema name "${parentSchemaName}". Make the title more descriptive.`,
        },
      ];
    }
  }

  return [];
};
