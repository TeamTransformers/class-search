<template>
  <v-expansion-panels>
  <v-expansion-panel>
        <v-expansion-panel-header>Course Name: #</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card class="d-flex flex-row justify-start align-center">
        <v-card-title>
          <v-simple-table>
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
                <tr v-for="item in courses" :key="item.name">
                  <td>{{ item.detail }}</td>
                  <td>{{ item.session }}</td>
                  <td>{{ item.section }}</td>
                  <td>{{ item.textbooks }}</td>
                  <td>{{ item.classnum }}</td>
                  <td>{{ item.seats }}</td>
                  <td>{{ item.status }}</td>
                  <td>{{ item.comp }}</td>
                  <td>{{ item.location }}</td>
                  <td>{{ item.days }}{{ item.time }}</td>
                  <td>{{ item.instruct }}</td>
                  <td>{{ item.consent }}</td>


                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-card-title>
        <!-- Insert Section Information Component here -->
        <b-table striped hover :items="items"></b-table>
      </v-card>
        </v-expansion-panel-content>
  </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
  export default {
    data () {
      return {
        courses: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
          },
          {
            name: 'Eclair',
            calories: 262,
          },
          {
            name: 'Cupcake',
            calories: 305,
          },
          {
            name: 'Gingerbread',
            calories: 356,
          },
          {
            name: 'Jelly bean',
            calories: 375,
          },
          {
            name: 'Lollipop',
            calories: 392,
          },
          {
            name: 'Honeycomb',
            calories: 408,
          },
          {
            name: 'Donut',
            calories: 452,
          },
          {
            name: 'KitKat',
            calories: 518,
          },
        ],
      }
    },
  }
</script>

<style>

</style>