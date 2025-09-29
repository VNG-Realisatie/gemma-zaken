import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";

const FeatureList = [
  {
    title: "Samen naar interoperabiliteit",
    Svg: require("@site/static/img/undraw_collaboration_dtwk.svg").default,
    description: (
      <>
        Maak uw organisatie wendbaarder en innovatiever door systemen
        probleemloos te laten samenwerken. Deze standaard biedt eenduidige
        richtlijnen en controle die dit mogelijk maken, met voorspelbaarheid,
        minder fouten en lagere kosten als resultaat.
      </>
    ),
  },
  {
    title: "Zekerheid vóóraf",
    Svg: require("@site/static/img/undraw_abstract_gk2d.svg").default,
    description: (
      <>
        Alle afspraken worden centraal en eenduidig vastgelegd in een
        ontwerp-contract, nog voordat er een regel code is geschreven. Hierdoor
        is het implementatieproces voorspelbaarder en betrouwbaarder uit te
        voeren.
      </>
    ),
  },
  {
    title: "Sneller in productie",
    Svg: require("@site/static/img/undraw_proud-coder_9prj.svg").default,
    description: (
      <>
        Implementeer sneller en met minder fouten. De API Suite biedt een set
        samenhangende API's die versiebeheer vereenvoudigt. Gebruik onze
        documentatie en tools voor een volledig testbare en robuuste integratie.
      </>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
