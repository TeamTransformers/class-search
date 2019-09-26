<template></template>

<script>
export default {
data: () => ({
    section: [
        {   //class Info//
            class_number: 1000,//key to finding correct section//
            section_info: [
                {
                Course_id: "15246" ,
                Subject: "Comp",
                Catalog_Number: "100",
                Section_number: "06",
                Title: "Computers: Thier Impact and Use", 
                Units: "3" ,
               
                Term: "Spring-2018",
                
                Component: "lecture",
                Session: "Regular",
                }
            ],
            meetings: [
                {
                meeting_number: "1",
                location: "JD1600" ,
                start_time: "0915h" ,
                end_time: "1045h",
                days: "MW"
                },
            ],
            instructor: [
                {
                instructor: "sevak.asadorian@csun.edu"
                }
            ],
            Availability: [
                {
                Enrollment_cap: 30,
                Enrollment_count: 10,
                Waitlist_cap: 20,
                Waitlist_count:0,
                }
            ],
            Final_Exam: [
                {
                Final_exam: true,
                Final_exam_date: "Dec 14, 2019",
                Final_exam_time:  "08:00Am - 10:00Am",
                Final_exam_loc:  "JD1600"
                }
            ],
            Enrollment_Information: [
                {
                    Course_Attri: "Array needed",

                }
            ],
            Notes: [
                {
                Subject_Notes: " Department Office: Jd 4503",
                Class_Notes: "Array needed"   
                }
            ],
            Course_Information: [
                {
                    Description:"Not open to computer Science majors.", 
                }
            ]
        }
        
    ]

})
}

</script>

<style>
</style>