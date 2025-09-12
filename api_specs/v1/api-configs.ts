
import type { OpenApiPlugin } from "docusaurus-plugin-openapi-docs";

// Define the configuration object for all your v1 APIs
const v1ApiConfigs: OpenApiPlugin.Options["config"] = {
  autorisaties: {
    specPath: "api_specs/v1/autorisaties/openapi.yaml",
    outputDir: "docs/v1/api-suite/autorisaties",
    sidebarOptions: {
      groupPathsBy: "tag",
      categoryLinkSource: "tag",
    },
  } satisfies OpenApiPlugin.Options,

  besluiten: {
    specPath: "api_specs/v1/besluiten/openapi.yaml",
    outputDir: "docs/v1/api-suite/besluiten",
    sidebarOptions: {
      groupPathsBy: "tag",
      categoryLinkSource: "tag",
    },
  } satisfies OpenApiPlugin.Options,
 
  documenten: {
    specPath: "api_specs/v1/documenten/openapi.yaml",
    outputDir: "docs/v1/api-suite/documenten",
    sidebarOptions: {
      groupPathsBy: "tag",
      categoryLinkSource: "tag",
    },
  } satisfies OpenApiPlugin.Options,

  // zaken: {
  //   specPath: "api_specs/v1/zaken/openapi.yaml",
  //   outputDir: "docs/v1/api-suite/zaken",
  //   sidebarOptions: {
  //     groupPathsBy: "tag",
  //     categoryLinkSource: "tag",
  //   },
  // } satisfies OpenApiPlugin.Options,

  // catalogi: {
  //   specPath: "api_specs/v1/catalogi/openapi.yaml",
  //   outputDir: "docs/v1/api-suite/catalogi",
  //   sidebarOptions: {
  //     groupPathsBy: "tag",
  //     categoryLinkSource: "tag",
  //   },
  // } satisfies OpenApiPlugin.Options,

};

// Export the object as the default export
export default v1ApiConfigs;
