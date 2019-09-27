<template>
    <v-container fluid>
      <v-data-iterator
      :items ="section"
      :items-per-page.sync= all
      hide-default-footer
      >
      <template v-slot:header = head>
        <v-toolbar 
        v-for="title in head.items"
        :key="title.name"
        class="mb-2"
        color="red"
        dark
        flat
       
        >
        <v-toolbar-title>
          {{title.Subject +" " + title.Catalog_Number + " - "+title.Title }}
          </v-toolbar-title>
        </v-toolbar>
      </template>
      <template v-slot:default="props">
        <v-row>
        <v-col
        v-for="item in props.items"
        :key="item.name"
        >

          <v-card dense>
            <v-card-title class="subheading font-weight-bold">Course information</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-item>
                <v-list-item-content>Class Number:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.class_number }}</v-list-item-content>
                <v-list-item-content>Section:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Section_number }}</v-list-item-content>
                <v-list-item-content>Units:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Units }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>Term:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Term }}</v-list-item-content>
                <v-list-item-content>Component:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Component }}</v-list-item-content>
                <v-list-item-content>Session:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Session }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-card-title class="subheading font-weight-bold">Meetings</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-item>
                <v-list-item-content>Meeting Number:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.meeting_number }}</v-list-item-content>
                <v-list-item-content>Location:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.location }}</v-list-item-content>
                
              </v-list-item>
              <v-list-item>
                <v-list-item-content>Days:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.days }}</v-list-item-content>
                <v-list-item-content>Time:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.start_time + " - " + item.end_time }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-card-title class="subheading font-weight-bold">{{"Instructor: "+item.instructor_name}}</v-card-title>
            <v-divider></v-divider>
            <v-divider></v-divider>
            <v-card-title class="subheading font-weight-bold">Enrollment</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-item>
                <v-list-item-content>Enrollment cap:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Enrollment_cap }}</v-list-item-content>
                <v-list-item-content>Waitlist cap:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Waitlist_cap }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>Enrollment count:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Enrollment_count }}</v-list-item-content>
                <v-list-item-content>Waitlist count:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Waitlist_count }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-card-title class="subheading font-weight-bold">Final Exam</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-item>
                <v-list-item-content>Final Exam:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Final_exam }}</v-list-item-content>
                <v-list-item-content>Final Exam Date:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Final_exam_date }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>Final Exam Time:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Final_exam_time }}</v-list-item-content>
                <v-list-item-content>Final Exam Loc:</v-list-item-content>
                <v-list-item-content class="align-end">{{ item.Final_exam_loc }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-card-title class="subheading font-weight-bold">Enrollemnt information</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-item>
              <v-list-item-content>Course Attribute :</v-list-item-content>
              <v-list-item-content class="align-end">{{ item.Course_Attri }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-card-title class="subheading font-weight-bold">Notes</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-item>
              <v-list-item-content>Subject Notes :</v-list-item-content>
              <v-list-item-content class="align-end">{{ item.Subject_Notes }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-list>
              <v-list-item>
              <v-list-item-content>Class Notes :</v-list-item-content>
              <v-list-item-content class="align-end">{{ item.Class_Notes }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-card-title class="subheading font-weight-bold">Course Information</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-item>
              <v-list-item-content>Subject Notes :</v-list-item-content>
              <v-list-item-content class="align-end">{{ item.Description }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <v-list>
              <v-list-item-content>Course will be offered in the following Terms:</v-list-item-content>
              <v-list-item-content class="align-end">{{ item.Course_Terms }}</v-list-item-content>
            </v-list>
          </v-card>
        </v-col>
        </v-row>
      </template>
      <template v-slot:footer>
        <v-toolbar
        class="mt-2"
        color="indigo"
        dark
        flat
        >
        <v-toolbar-title class="subheading">@2019</v-toolbar-title>
        </v-toolbar>
      </template>
      </v-data-iterator>
  </v-container>
</template>

<script>
export default {
data: () => ({
    section: [
      {   //class Info//
        class_number: 1010,//key to finding correct section//
        Course_id: "15246" ,
        Subject: "Comp",
        Catalog_Number: "100",
        Section_number: "06",
        Title: "Computers: Thier Impact and Use", 
        Units: "3" ,            
        Term: "Spring-2018",               
        Component: "lecture",
        Session: "Regular",

        meeting_number: "1",
        location: "JD1600" ,
        start_time: "09:15" ,
        end_time: "10:45",
        days: "MW",

        instructor_name: "sevak asadorian",
        instructor_email: "sevak.asadorian@csun.edu",
    

        Enrollment_cap: 30,
        Enrollment_count: 10,
        Waitlist_cap: 20,
        Waitlist_count:0,

        Final_exam: true,
        Final_exam_date: "Dec 14, 2019",
        Final_exam_time:  "08:00Am - 10:00Am",
        Final_exam_loc:  "JD1600",

        Course_Attri: "Array needed",

        Subject_Notes: " Department Office: Jd 4503",
        Class_Notes: "Array needed",   

        Description:"Not open to computer Science majors.", 
        Course_Terms:"Fall Semester 2019, Spring Semester 2020"
                
            
        },
        
    ],
  }),
}
</script>