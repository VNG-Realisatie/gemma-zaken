const fs = require("node:fs");
const path = require("node:path");
const { Spectral, Bundle } = require("@stoplight/spectral-core");
const {
  bundleAndLoadRuleset,
} = require("@stoplight/spectral-ruleset-bundler/with-loader");
const yaml = require("yaml");

describe("ZGW Composition Rules", () => {
  let spectral;

  beforeAll(async () => {
    spectral = new Spectral();
    const rulesetFilepath = path.join(
      __dirname,
      "../zgw-api-design-rules.yaml",
    );
    spectral.setRuleset(
      await bundleAndLoadRuleset(rulesetFilepath, { fs, fetch }),
    );
  });

  describe("no-remote-refs", () => {
    test("should pass with local refs", async () => {
      const testCase = yaml.parse(`
        components:
          schemas:
            User:
              $ref: "#/components/schemas/BaseUser"
            Profile:
              allOf:
                - $ref: "#/components/schemas/BaseProfile"
                - type: object
      `);

      const results = await spectral.run(testCase);
      const noRemoteRefResults = results.filter(
        (result) => result.code === "no-remote-refs",
      );
      expect(noRemoteRefResults).toHaveLength(0);
    });

    test("should fail with remote refs", async () => {
      const testCase = yaml.parse(`
        components:
          schemas:
            User:
              $ref: "https://example.com/schemas/BaseUser"
      `);

      const results = await spectral.run(testCase);
      const noRemoteRefResults = results.filter(
        (result) => result.code === "no-remote-refs",
      );
      expect(noRemoteRefResults).toHaveLength(1);
    });
  });
});
