<template>
  <v-container fluid>
    <v-data-iterator :items="section" hide-default-footer>
      <template v-slot:header="head">
        <v-toolbar
          v-for="title in head.items"
          :key="title.name"
          color="red draken-4"
          dark
          :elevation="24"
        >
          <v-btn class="mx-0" fab x-small color="red draken-4" dark :elevation="24">
            <v-icon dark>mdi-arrow-left</v-icon>
          </v-btn>
          <div class="text-center">
            <v-toolbar-title
              class="caption font-weight-bold text-wrap text-center"
            >{{title.Subject +":" + title.Catalog_Number +" "+title.Title }}</v-toolbar-title>
          </div>
        </v-toolbar>
      </template>
      <template v-slot:default="props">
        <v-row>
          <v-col v-for="item in props.items" :key="item.name">
            <v-expansion-panels v-model="item.panel" multiple accordion>
              <v-expansion-panel>
                <v-expansion-panel-header
                  class="caption font-weight-bold text-center grey"
                >Course Information</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title
                          class="caption font-weight-black text-wrap text-center"
                        >Class Number</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black text-wrap text-center"
                        >{{item.class_number}}</v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Section</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Section_number}}</v-list-item-subtitle>
                      </v-list-item-content>

                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Instructor</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black text-wrap text-center"
                        >{{item.instructor_name}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content class="caption text-center">
                        <v-list-item-title class="caption font-weight-black">Term</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black text-wrap text-center"
                        >{{item.Term}}</v-list-item-subtitle>
                      </v-list-item-content>

                      <v-list-item-content class="caption text-center">
                        <v-list-item-title class="caption font-weight-black">Status</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                          v-if="item.Enrollment_cap > item.Enrollment_count"
                        >
                          Open
                          <v-icon fab small color="green">mdi-checkbox-marked-circle</v-icon>
                        </v-list-item-subtitle>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                          v-else-if="item.Enrollment_cap <= item.Enrollment_count + item.Waitlist_cap > item.Waitlist_count"
                        >
                          Waitlist
                          <v-icon fab small color="yellow">mdi-clipboard-list-outline</v-icon>
                        </v-list-item-subtitle>
                        <v-list-item-subtitle class="caption font-weight-black" v-else>
                          Closed
                          <v-icon fab small color="red draken-4">mdi-cancel</v-icon>
                        </v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="caption text-center">
                        <v-list-item-title class="caption font-weight-black">Units</v-list-item-title>
                        <v-list-item-subtitle class="caption font-weight-black">{{item.Units}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header class="caption font-weight-bold text-center grey">Meetings</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list>
                    <v-list-item>
                      <v-list-item-content class="text-center">
                        <v-list-item-title
                          class="caption font-weight-black text-wrap text-center"
                        >Number of Meetings</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.meeting_number}}</v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Location</v-list-item-title>
                        <v-list-item-subtitle class="caption font-weight-black">{{item.location}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Days</v-list-item-title>
                        <v-list-item-subtitle class="caption font-weight-black">{{item.days}}</v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Time</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.start_time + " - " + item.end_time}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header
                  class="caption font-weight-bold text-center grey"
                >Class Avaliability</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list>
                    <v-list-item>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Class Limit</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Enrollment_cap}}</v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Waitlist Limit</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Waitlist_cap}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Current Capacity</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Enrollment_count}}</v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Waitlist Capacity</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Waitlist_count}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header
                  class="caption font-weight-bold text-center grey"
                >Final Exam</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list>
                    <v-list-item>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Fianl Exam</v-list-item-title>
                        <v-list-item-subtitle class="caption font-weight-black">{{item.Final_exam}}</v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Final Exam Date</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Final_exam_date}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Final Exam Time</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black text-wrap text-center"
                        >{{item.Final_exam_time}}</v-list-item-subtitle>
                      </v-list-item-content>
                      <v-list-item-content class="text-center">
                        <v-list-item-title class="caption font-weight-black">Final Exam Loc</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Final_exam_loc}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header
                  class="caption font-weight-bold text-center grey"
                >Enrollment Infromation</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list>
                    <v-list-item>
                      <v-list-item-content class="text-left">
                        <v-list-item-title class="caption font-weight-black">Course Attribute</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black"
                        >{{item.Course_Attri}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header class="caption font-weight-bold text-center grey">Notes</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list>
                    <v-list-item>
                      <v-list-item-content class="text-left">
                        <v-list-item-title class="caption font-weight-black">Subject Notes</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black text-wrap text-center"
                        >{{item.Subject_Notes}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content class="text-left">
                        <v-list-item-title class="caption font-weight-black">Class Notes</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black text-wrap text-center"
                        >{{item.Class_Notes}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header
                  class="caption font-weight-bold text-center grey"
                >Course Terms</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list>
                    <v-list-item>
                      <v-list-item-content class="text-left">
                        <v-list-item-title
                          class="caption font-weight-black text-wrap text-center"
                        >Course will be offered in the following Terms</v-list-item-title>
                        <v-list-item-subtitle
                          class="caption font-weight-black text-wrap text-center"
                        >{{item.Course_Terms}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-col>
        </v-row>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    section: [
      {
        //class Info//
        panel: [0, 1],
        class_number: 152489, //key to finding correct section//
        Course_id: "15246",
        Subject: "Comp",
        Catalog_Number: "100",
        Section_number: "06",
        Title: "Computers: Thier Impact and Use",
        Units: "3",
        Term: "Spring-2018",
        Component: "lecture",
        Session: "Regular",

        meeting_number: "1",
        location: "JD1600",
        start_time: "09:15",
        end_time: "10:45",
        days: "MW",

        instructor_name: "sevak asadorian",
        instructor_email: "sevak.asadorian@csun.edu",

        Enrollment_cap: 30,
        Enrollment_count: 30,
        Waitlist_cap: 20,
        Waitlist_count: 0,

        Final_exam: true,
        Final_exam_date: "Dec 14, 2019",
        Final_exam_time: "08:00Am - 10:00Am",
        Final_exam_loc: "JD1600",

        Course_Attri: "Array needed",

        Subject_Notes:
          " Department Office: Jd 4503 in need of more description in order to tedt the flexability of the screen space we are given to us and opperate",
        Class_Notes: "write something write something write something write something write something write something write something write something write somethingwrite something vv",

        Description: "Not open to computer Science majors.",
        Course_Terms: "Fall Semester 2019, Spring Semester 2020"
      }
    ]
  })
};
</script>