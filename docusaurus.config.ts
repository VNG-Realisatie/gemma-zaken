// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

import type * as Preset from "@docusaurus/preset-classic";
import type { Config } from "@docusaurus/types";
import type * as Plugin from "@docusaurus/types/src/plugin";
import type * as OpenApiPlugin from "docusaurus-plugin-openapi-docs";
import {themes as prismThemes} from 'prism-react-renderer';
// import { remarkKroki } from 'remark-kroki';

const config: Config = {
  title: "API's voor zaakgericht werken",
  tagline: "De officiële standaard met gids, referentiedocumentatie en tools.",
  url: "https://vng-realisatie.github.io/",
  baseUrl: "/gemma-zaken",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "vng-realisatie", // Your GitHub org/user name.
  projectName: "gemma-zaken", // Your repo name.
  trailingSlash: false, // explicit trailing slash

  //
  // NOTE development deployment -- noIndex
  //
  noIndex: true,

  i18n: {
    defaultLocale: 'nl',
    locales: ['nl', 'en'],
  },
  
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // id: "default", // ommitted, because it's the default docs instance
          path: "docs",
          routeBasePath: "/",
          sidebarPath: require.resolve("./sidebars.ts"),
          remarkPlugins: [
              // [
              // remarkKroki,
              // {
              //   alias: ['d2'],
              //   target: 'mdx3',
              //   server: 'https://kroki.io',
              //   outputFormat: 'svg',
              //   headers: {
              //     'Kroki-Diagram-Options-Theme': '0',
              //     'Kroki-Diagram-Options-Dark-Theme': '200',
              //     'Kroki-Diagram-Options-Pad': '0',
              //     'Kroki-Diagram-Options-Scale': '1',
              //   }
              // }
              // ]
          ]

          //rehypePlugins: [[rehypeD2, {}]],
        },
        theme: {
          customCss: require.resolve("./src/css/vng-huisstijl.css"),
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig:
    {
      colorMode: {
          respectPrefersColorScheme: true,
      },
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      announcementBar: {
        id: 'support_us',
        content:
          'Deze documentatie wordt momenteel bijgewerkt en is nog niet up-to-date.',
        isCloseable: false,
      },      
      navbar: {
        title: "ZGW API's",
        logo: {
          alt: "VNG logo",
          src: "img/vng_logo.svg",
          srcDark: "img/vng_logo_alt.svg",
        },
        items: [
          {
            type: "doc",
            docId: "gids/index",
            position: "left",
            label: "Gids",
          },
          {
            type: "doc",
            docId: "index",
            position: "left",
            label: "API Suite",
            docsPluginId: "api",
          },
          {
            type: "doc",
            docId: "community/index",
            position: "left",
            label: "Community",
          },
          {
            type: "docsVersionDropdown",
            docsPluginId: "api",
            position: "right",
          },
          {
            href: "https://github.com/vng-realisatie/gemma-zaken",
            position: "right",
            className: "header-github-link",
            "aria-label": "GitHub repository"
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Standaard",
            items: [
              {
                label: "Referentie",
                to: "/contributing",
              },
              {
                label: "Releases",
                href: "https://github.com/vng-realisatie/gemma-zaken/releases",
              },
              {
                label: "Design rules",
                to: "/contributing",
              },
              {
                label: "Tools",
                to: "/contributing",
              },
            ]
          },
          {
            title: "Project",
            items: [
              {
                label: "Over de ZGW API standaard",
                to: "/contributing",
              },
              {
                label: "Besluitenlogboek",
                to: "/adrs",
              },
              {
                label: "Doe mee",
                to: "/contributing",
              },
              {
                label: "Contact",
                to: "/contact",
              },
            ]
          },
          {
            title: "Context",
            items: [
              {
                label: "GEMMA Online",
                href: "https://www.gemmaonline.nl/wiki/Thema-architectuur_Zaakgericht_werken",
              },
              {
                label: "'Pas toe, leg uit' standaarden",
                href: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht",
              },
              {
                label: "Praktijkvoorbeelden",
                to: "/voorbeelden",
              },
              {
                label: "Common Ground",
                href: "https://www.commonground.nl",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} VNG Realisatie`,
      },
      prism: {
        additionalLanguages: [
          "bash",
          "csharp",
          "java",
          "json",
          "php",
          "powershell",
        ],
      },
      languageTabs: [
        {
          highlight: "bash",
          language: "curl",
          logoClass: "curl",
        },
        {
          highlight: "python",
          language: "python",
          logoClass: "python",
        },
        {
          highlight: "javascript",
          language: "nodejs",
          logoClass: "nodejs",
        },
        {
          highlight: "java",
          language: "java",
          logoClass: "java",
        },
      ],
    //   zoom: {
    //     selectors: ['.panzoom-element'],
    //     wrap: true,
    //     timeout: 1000
    //   }
    } satisfies Preset.ThemeConfig,

    plugins: [
        [ "@docusaurus/plugin-content-docs",
            {
                id: "api",
                path: "api_docs",
                routeBasePath: "apis/",
                sidebarPath: "./api_sidebars.ts",
                docItemComponent: "@theme/ApiItem", // Derived from docusaurus-theme-openapi

                versions: {
                  // 'current' is the special key for the docs in your `path` folder ('api_docs').
                  current: {
                      label: "Next (1.6.0) 🛠️",
                      // You can optionally change the route path for this version too
                      path: '/next',
                  },
                // If you had other, older versions, they would be listed here
                // e.g., "1.0": { label: "v1.0" },
              },

            } satisfies Plugin.PluginOptions,
        ],
        [ "docusaurus-plugin-openapi-docs",
          {
            id: "openapi",
            docsPluginId: "api",
            config: {
              autorisaties: {
                specPath: "api_specs/autorisaties/openapi.yaml",
                outputDir: "api_docs/autorisaties",
                sidebarOptions: {
                  groupPathsBy: "tag",
                  categoryLinkSource: "tag",
                },
              } satisfies OpenApiPlugin.Options,
            }
          } satisfies Plugin.PluginOptions,
        ]
    ],


  markdown: {
    mermaid: true,
    remarkRehypeOptions: {
      footnoteLabel: 'Voetnoten',
    },
  },

  themes: ['@docusaurus/theme-mermaid', "docusaurus-theme-openapi-docs"],
};

export default async function createConfig() {
  return config;
}

