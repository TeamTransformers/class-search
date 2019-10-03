<template>
  <v-data-table
    :headers="headers"
    :items="courses"
    :items-per-page="5"
    :hide-default-footer="true"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        { text: "Detail", align: "left", sortable: false, value: "name" },
        { text: "Session", align: "center", value: "sess" },
        { text: "Sect", align: "center", value: "sect" },
        { text: "Text", align: "center", value: "text" },
        { text: "Class#", align: "center", value: "class" },
        { text: "Seats available", align: "center", value: "seat" },
        { text: "Enrolled status", align: "center", value: "status" },
        { text: "Comp", align: "center", value: "comp" },
        { text: "Loc", align: "center", value: "map" },
        { text: "Days", align: "center", value: "day" },
        { text: "Time", align: "center", value: "time" },
        { text: "Instructor", align: "center", value: "instruct" },
        { text: "Consent", align: "center", value: "consent" }
      ],
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
  }
};
</script>