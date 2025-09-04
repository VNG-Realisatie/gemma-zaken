import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const sidebar: SidebarsConfig = {
  apisidebar: [
    {
      type: "doc",
      id: "autorisaties/autorisaties-api",
    },
    {
      type: "category",
      label: "applicaties",
      link: {
        type: "doc",
        id: "autorisaties/applicaties",
      },
      items: [
        {
          type: "doc",
          id: "autorisaties/applicatie-list",
          label:
            "Geef een collectie van applicaties, met ingesloten autorisaties.",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "autorisaties/applicatie-create",
          label:
            "Registreer een applicatie met een bepaalde set van autorisaties.",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "autorisaties/applicatie-consumer",
          label: "Vraag een applicatie op, op basis van clientId",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "autorisaties/applicatie-read",
          label: "Vraag een applicatie op, met ingesloten autorisaties.",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "autorisaties/applicatie-update",
          label: "Werk de applicatie bij.",
          className: "api-method put",
        },
        {
          type: "doc",
          id: "autorisaties/applicatie-partial-update",
          label: "Werk (een deel van) de applicatie bij.",
          className: "api-method patch",
        },
        {
          type: "doc",
          id: "autorisaties/applicatie-delete",
          label: "Verwijder een applicatie met de bijhorende autorisaties.",
          className: "api-method delete",
        },
      ],
    },
  ],
};

export default sidebar.apisidebar;
