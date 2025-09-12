import React from "react";
import NavbarItem from "@theme-original/NavbarItem";
import { useActivePlugin } from "@docusaurus/plugin-content-docs/client";

export default function NavbarItemWrapper(props) {
  const activePlugin = useActivePlugin();

  // Add this console.log to see the new hook in action
  console.log(
    "Active Plugin ID:",
    activePlugin,
    "| Prop needed:",
    props.activeWhen,
    // "| docsversion:",
    // useDocsVersion,
  );

  // If the item has an 'activeWhen' prop, check if it matches the active plugin's ID.
  if (props.activeWhen) {
    // If there's no active plugin OR the ID doesn't match, don't render.
    if (!activePlugin || props.activeWhen !== activePlugin.pluginId) {
      return null;
    }
  }

  return (
    <>
      <NavbarItem {...props} />
    </>
  );
}
