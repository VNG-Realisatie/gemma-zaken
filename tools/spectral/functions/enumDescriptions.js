export default (schema) => {
  const enumValues = schema.enum;
  const descriptionKeys = Object.keys(schema["x-enumDescriptions"]);

  const errors = [];

  // Check if arrays have same length
  if (enumValues.length !== descriptionKeys.length) {
    return [
      {
        message: `Number of enum values (${enumValues.length}) does not match number of descriptions (${descriptionKeys.length})`,
      },
    ];
  }

  // Check if all enum values have matching descriptions
  for (const enumValue of enumValues) {
    if (!schema["x-enumDescriptions"].hasOwnProperty(enumValue)) {
      return [
        {
          message: `Enum value "${enumValue}" has no matching description`,
        },
      ];
    }
  }

  // Check if all descriptions have matching enum values
  for (const descKey of descriptionKeys) {
    if (!enumValues.includes(descKey)) {
      return [
        {
          message: `Description key "${descKey}" has no matching enum value`,
        },
      ];
    }
  }

  return errors;
};
