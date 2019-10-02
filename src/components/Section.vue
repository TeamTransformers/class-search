<template>
  <v-simple-table 
    dense="dense" 
    :fixed-header="fixedHeader"
    :height="height">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Detail</th>
          <th class="text-left">Session</th>
          <th class="text-left">Section</th>
          <th class="text-left">Textbooks</th>
          <th class="text-left">Class #</th>
          <th class="text-left">Seats available</th>
          <th class="text-left">Enrolled status</th>
          <th class="text-left">Comp</th>
          <th class="text-left">Location</th>
          <th class="text-left">Days/Time</th>
          <th class="text-left">Instructor</th>
          <th class="text-left">Consent</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in courses" :key="item.session">
          <td>{{ item.detail }}</td>
          <td class="text-center">{{ item.session }}</td>
          <td class="text-center">{{ item.section }}</td>
          <td>{{ item.textbook }}</td>
          <td class="text-center">{{ item.classnum }}</td>
          <td class="text-center">{{ item.seats }}</td>
          <td class="text-center">{{ item.status }}</td>
          <td class="text-center">{{ item.comp }}</td>
          <td class="text-center">{{ item.loc }}</td>
          <td>{{ item.day }}{{ item.time }}</td>
          <td>{{ item.instructor }}</td>
          <td>{{ item.content }}</td>
          </tr>
      </tbody>
    </template>  
  </v-simple-table>
</template>
          

<script>
  export default {
    data: () => ({
      dense: false,
      fixedHeader: false,
      height: 300,
      courses: [
        {
          detail: null,
          session: 1,
          section: 1,
          textbook: null,
          classnum: 16320,
          seats: '-10',
          status: 'closed',
          comp: 'LEC',
          loc: 'JD3510',
          day: 'Tu/Th',
          instructor: 'McInhenny, Robert D',
          content: null,
        },
        {
          detail: null,
          session: 1,
          section: 2,
          textbook: null,
          classnum: 16321,
          seats: '-2',
          status: 'closed',
          comp: 'LEC',
          loc: 'JD1618',
          day: 'Tu/Th',
          instructor: 'Lazik, George L',
          content: null,
        },
        {
          detail: null,
          session: 1,
          section: 3,
          textbook: null,
          classnum: 16839,
          seats: '-7',
          status: 'closed',
          comp: 'LEC',
          loc: 'JD1618',
          day: 'Tu/Th',
          instructor: 'Lazik, George L',
          content: null,
        },
        {
          detail: null,
          session: 1,
          section: 4,
          textbook: null,
          classnum: 17067,
          seats: '0',
          status: 'closed',
          comp: 'LEC',
          loc: 'JD1600',
          day: 'Tu/Th',
          instructor: 'Lazik, George L',
          content: null,
        },
        {
          detail: null,
          session: 1,
          section: 5,
          textbook: null,
          classnum: 21293,
          seats: '-2',
          status: 'closed',
          comp: 'LEC',
          loc: 'JD3510',
          day: 'Tu',
          instructor: 'Bhatt, Vijay J',
          content: null,
        },
      ],
    }),
  }
</script>