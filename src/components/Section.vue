<template>
  <v-app>
      <v-list v-for="data in courses" :key="data">
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="caption font-weight-black text-wrap text-center">Status</v-list-item-title>
            <v-list-item-subtitle
              class="caption font-weight-black text-wrap text-center"
            >{{data.status}}</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-content>
            <v-list-item-title class="caption font-weight-black text-wrap text-center">Section</v-list-item-title>
            <v-list-item-subtitle
              class="caption font-weight-black text-wrap text-center"
            >{{data.sect}}</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-content>
            <v-btn icon x-small color="blue" @click="send">
              <v-icon dark>mdi-book-open-page-variant</v-icon>
            </v-btn>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="caption font-weight-black text-wrap text-center">instructor</v-list-item-title>
            <v-list-item-subtitle
              class="caption font-weight-black text-wrap text-center"
            >{{data.instruct}}</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-content>
            <v-list-item-title class="caption font-weight-black text-wrap text-center">Time</v-list-item-title>
            <v-list-item-subtitle
              class="caption font-weight-black text-wrap text-center"
            >{{data.day+" "+data.time}}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
      </v-list>
  </v-app>
</template>

<script>
import SectionPage from "./SectionPage";
export default {
  data() {
    return {
      open: 1,
      courses: [
        {
          name: null,
          sess: 1,
          sect: "01",
          text: null,
          class: 16320,
          seat: "-10",
          status: "closed",
          comp: "LEC",
          map: "JD3510",
          day: "Tu/Th",
          time: "02:00pm-03:15pm",
          instruct: "McInhenny, Robert D",
          consent: null
        },
        {
          name: null,
          sess: 1,
          sect: "02",
          text: null,
          class: 16321,
          seat: "-2",
          status: "closed",
          comp: "LEC",
          map: "JD1618",
          day: "Tu/Th",
          time: "02:00pm-03:15pm",
          instruct: "Lazik, George L",
          consent: null
        },
        {
          name: null,
          sess: 1,
          sect: "03",
          text: null,
          class: 16839,
          seat: "-7",
          status: "closed",
          comp: "LEC",
          map: "JD1618",
          day: "Tu/Th",
          time: "02:00pm-03:15pm",
          instruct: "Lazik, George L",
          consent: null
        },
        {
          name: null,
          sess: 1,
          sect: "04",
          text: null,
          class: 17067,
          seat: "0",
          status: "closed",
          comp: "LEC",
          map: "JD1600",
          day: "Tu/Th",
          time: "02:00pm-03:15pm",
          instruct: "Lazik, George L",
          consent: null
        },
        {
          name: null,
          sess: 1,
          sect: "05",
          text: null,
          class: 21293,
          seat: "-2",
          status: "closed",
          comp: "LEC",
          map: "JD3510",
          day: "Tu",
          time: "02:00pm-03:15pm",
          instruct: "Bhatt, Vijay J",
          consent: null
        }
      ]
    };
  },
  methods:{
        send(){
            this.$emit('Switch');
        }
  },
  components: {
    SectionPage
  }
};
</script>