<template>
  <v-expansion-panels>
  <v-expansion-panel>
        <v-expansion-panel-header>Course Name: #</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card class="d-flex flex-row justify-start align-center">
        <v-card-title>
          <Section></Section>
        </v-card-title>
        <!-- Insert Section Information Component here -->  
      </v-card>
        </v-expansion-panel-content>
  </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>

import Section from './Section'

  export default {
    components: { Section },
    data: () => ({
      
    }),
  }
</script>


<style>

</style>