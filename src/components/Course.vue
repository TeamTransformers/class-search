<template>
  <v-expansion-panel>
        <v-expansion-panel-header class="grey">Course Name: #</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card class="d-flex flex-row justify-start align-center">
          <Section @Switch="Upone"></Section>
        <!-- Insert Section Information Component here -->  
      </v-card>
        </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>

import Section from './Section'

  export default {
    components: { Section },
    data(){
      
    },
    methods:{
       Upone(){
         this.$emit('next');
       }
    },
  }
</script>


<style>

</style>
