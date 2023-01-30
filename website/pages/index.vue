<template>
  <v-col cols="12" sm="8" md="6" justify="center" class="mx-auto">
    <v-card class="py-5 px-5">
      <v-img
        lazy-src="figure1.png"
        max-height="400"
        max-width="600"
        src="figure1.png"
      ></v-img>
    </v-card>
    <v-card>
      <v-card-title class="headline"> Feedback Log Tool </v-card-title>
      <v-card-text>
        <p>
          Feedack logs are used to track the interaction between practitioners
          and experts to create a defensible and auditable machine learning
          ecosystem.
        </p>
        <p>
          This is an openly available tool for creating feedback logs. There are
          two complementary software tools:
        </p>

        <ol>
          <li>
            This web interface to view and update feedback logs, designed for
            use by experts and machine learning practioners. An example log
            based on TV content recommendation is accessible
            <NuxtLink to="/example">here</NuxtLink>, while a blank log for you
            to fill out is available <NuxtLink to="/feedback">here</NuxtLink>.
          </li>
          <li>
            A command line interface (CLI) designed for use by practitioners to
            track updates to code based on expert feedback. Accessible in the
            GitHub repo
            <a
              href="https://github.com/barkermrl/feedback-log"
              target="_blank"
              rel="noopener noreferrer"
              >here</a
            >.
          </li>
        </ol>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn color="primary" nuxt to="/example">Example</v-btn>
        <v-btn color="primary" nuxt to="/feedback">Make my own</v-btn>
      </v-card-actions>
    </v-card>
  </v-col>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>
