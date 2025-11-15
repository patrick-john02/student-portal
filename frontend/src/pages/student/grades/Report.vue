<script setup lang="ts">
import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbSeparator,
  BreadcrumbPage,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"

import {
  Bell,
  Award,
  Download,
  Printer,
  Mail,
  TrendingUp,
  Calendar,
  User,
  School,
} from "lucide-vue-next"

const userRole = "Student"

// Student Information
const studentInfo = {
  name: "Maria Santos",
  studentId: "2024-STEM-001",
  gradeLevel: "Grade 12",
  section: "STEM-A",
  schoolYear: "2024-2025",
  quarter: "Third Quarter",
}

// Detailed Grade Report
const gradeReport = [
  {
    subject: "Mathematics",
    teacher: "Mr. Juan dela Cruz",
    credits: 4,
    grades: {
      written: 88,
      performance: 92,
      quarterly: 90,
    },
    letterGrade: "A",
    remarks: "Excellent",
  },
  {
    subject: "Science",
    teacher: "Ms. Ana Reyes",
    credits: 4,
    grades: {
      written: 85,
      performance: 90,
      quarterly: 88,
    },
    letterGrade: "B+",
    remarks: "Good",
  },
  {
    subject: "English",
    teacher: "Mrs. Sofia Garcia",
    credits: 4,
    grades: {
      written: 90,
      performance: 94,
      quarterly: 92,
    },
    letterGrade: "A",
    remarks: "Excellent",
  },
  {
    subject: "Filipino",
    teacher: "Mr. Pedro Santos",
    credits: 4,
    grades: {
      written: 83,
      performance: 87,
      quarterly: 85,
    },
    letterGrade: "B",
    remarks: "Good",
  },
  {
    subject: "Social Studies",
    teacher: "Ms. Maria Lopez",
    credits: 3,
    grades: {
      written: 86,
      performance: 88,
      quarterly: 87,
    },
    letterGrade: "B+",
    remarks: "Good",
  },
  {
    subject: "Physical Education",
    teacher: "Coach Mike Tan",
    credits: 2,
    grades: {
      written: 92,
      performance: 96,
      quarterly: 94,
    },
    letterGrade: "A",
    remarks: "Excellent",
  },
]

// Calculate overall statistics
const totalCredits = gradeReport.reduce((sum, s) => sum + s.credits, 0)
const weightedSum = gradeReport.reduce(
  (sum, s) => sum + s.grades.quarterly * s.credits,
  0
)
const generalAverage = Math.round(weightedSum / totalCredits)
const gpa = (weightedSum / totalCredits / 25).toFixed(2)

const getGradeColor = (grade: number) => {
  if (grade >= 90) return "text-green-600"
  if (grade >= 80) return "text-blue-600"
  if (grade >= 75) return "text-yellow-600"
  return "text-red-600"
}

const getGradeBg = (grade: number) => {
  if (grade >= 90) return "bg-green-50"
  if (grade >= 80) return "bg-blue-50"
  if (grade >= 75) return "bg-yellow-50"
  return "bg-red-50"
}
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- HEADER -->
      <header
        class="flex h-16 shrink-0 items-center gap-2 px-4 
               transition-[width,height] ease-linear"
      >
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="/student/dashboard">
                Student
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="/student/grades">
                Grades
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>Report</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>

        <div class="ml-auto flex items-center gap-2 px-4">
          <Button variant="outline" size="sm">
            <Bell class="h-4 w-4" />
          </Button>
        </div>
      </header>

      <!-- MAIN CONTENT -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Page Header -->
        <div class="rounded-lg border bg-card p-6">
          <div
            class="flex flex-col md:flex-row md:items-center md:justify-between gap-4"
          >
            <div>
              <h2 class="text-3xl font-bold">Official Grade Report</h2>
              <p class="text-muted-foreground mt-2">
                {{ studentInfo.quarter }} • Academic Year {{ studentInfo.schoolYear }}
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Printer class="mr-2 h-4 w-4" />
                Print
              </Button>
              <Button variant="outline">
                <Mail class="mr-2 h-4 w-4" />
                Email
              </Button>
              <Button>
                <Download class="mr-2 h-4 w-4" />
                Download PDF
              </Button>
            </div>
          </div>
        </div>

        <!-- Report Card -->
        <Card>
          <CardContent class="p-0">
            <!-- School Header -->
            <div class="p-6 border-b bg-gradient-to-r from-blue-50 to-background">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-4">
                  <div
                    class="h-16 w-16 bg-primary/10 rounded-lg flex items-center justify-center"
                  >
                    <School class="h-8 w-8 text-primary" />
                  </div>
                  <div>
                    <h3 class="text-xl font-bold">Philippine Science High School</h3>
                    <p class="text-sm text-muted-foreground">
                      Taguig City, Metro Manila
                    </p>
                  </div>
                </div>
                <Badge class="text-lg px-4 py-2">Official Report Card</Badge>
              </div>
            </div>

            <!-- Student Information -->
            <div class="p-6 border-b bg-muted/30">
              <div class="grid md:grid-cols-2 gap-4">
                <div class="space-y-2">
                  <div class="flex items-center gap-2">
                    <User class="h-4 w-4 text-muted-foreground" />
                    <span class="text-sm font-semibold">Student Name:</span>
                    <span class="text-sm">{{ studentInfo.name }}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <Award class="h-4 w-4 text-muted-foreground" />
                    <span class="text-sm font-semibold">Student ID:</span>
                    <span class="text-sm">{{ studentInfo.studentId }}</span>
                  </div>
                </div>
                <div class="space-y-2">
                  <div class="flex items-center gap-2">
                    <School class="h-4 w-4 text-muted-foreground" />
                    <span class="text-sm font-semibold">Grade & Section:</span>
                    <span class="text-sm">
                      {{ studentInfo.gradeLevel }} - {{ studentInfo.section }}
                    </span>
                  </div>
                  <div class="flex items-center gap-2">
                    <Calendar class="h-4 w-4 text-muted-foreground" />
                    <span class="text-sm font-semibold">School Year:</span>
                    <span class="text-sm">{{ studentInfo.schoolYear }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Grades Table -->
            <div class="overflow-x-auto">
              <table class="w-full">
                <thead class="bg-muted/50">
                  <tr>
                    <th class="p-4 text-left text-sm font-semibold">Subject</th>
                    <th class="p-4 text-left text-sm font-semibold">Teacher</th>
                    <th class="p-4 text-center text-sm font-semibold">Credits</th>
                    <th class="p-4 text-center text-sm font-semibold">
                      Written Works (40%)
                    </th>
                    <th class="p-4 text-center text-sm font-semibold">
                      Performance Tasks (60%)
                    </th>
                    <th class="p-4 text-center text-sm font-semibold">
                      Quarterly Grade
                    </th>
                    <th class="p-4 text-center text-sm font-semibold">
                      Letter Grade
                    </th>
                    <th class="p-4 text-center text-sm font-semibold">Remarks</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(subject, index) in gradeReport"
                    :key="index"
                    :class="[
                      'border-b',
                      index % 2 === 0 ? 'bg-background' : 'bg-muted/20',
                    ]"
                  >
                    <td class="p-4 font-medium">{{ subject.subject }}</td>
                    <td class="p-4 text-sm text-muted-foreground">
                      {{ subject.teacher }}
                    </td>
                    <td class="p-4 text-center">{{ subject.credits }}</td>
                    <td class="p-4 text-center">
                      <span :class="['font-semibold', getGradeColor(subject.grades.written)]">
                        {{ subject.grades.written }}
                      </span>
                    </td>
                    <td class="p-4 text-center">
                      <span
                        :class="['font-semibold', getGradeColor(subject.grades.performance)]"
                      >
                        {{ subject.grades.performance }}
                      </span>
                    </td>
                    <td class="p-4 text-center">
                      <Badge
                        :class="[
                          'font-bold text-base',
                          getGradeBg(subject.grades.quarterly),
                        ]"
                      >
                        {{ subject.grades.quarterly }}
                      </Badge>
                    </td>
                    <td class="p-4 text-center">
                      <Badge variant="outline" class="font-semibold">
                        {{ subject.letterGrade }}
                      </Badge>
                    </td>
                    <td class="p-4 text-center text-sm">
                      {{ subject.remarks }}
                    </td>
                  </tr>
                </tbody>
                <tfoot class="bg-muted/50 font-semibold">
                  <tr>
                    <td colspan="2" class="p-4 text-right">Total Credits:</td>
                    <td class="p-4 text-center">{{ totalCredits }}</td>
                    <td colspan="2" class="p-4 text-right">General Average:</td>
                    <td class="p-4 text-center">
                      <Badge
                        :class="['font-bold text-base', getGradeBg(generalAverage)]"
                      >
                        {{ generalAverage }}
                      </Badge>
                    </td>
                    <td class="p-4 text-center">
                      <Badge variant="outline" class="font-semibold">
                        {{ generalAverage >= 90 ? 'A' : generalAverage >= 80 ? 'B' : 'C' }}
                      </Badge>
                    </td>
                    <td class="p-4 text-center">
                      {{ generalAverage >= 90 ? 'Excellent' : 'Good' }}
                    </td>
                  </tr>
                </tfoot>
              </table>
            </div>

            <!-- Summary Section -->
            <div class="p-6 border-t bg-muted/30">
              <div class="grid md:grid-cols-3 gap-6">
                <div class="text-center p-4 bg-background rounded-lg border">
                  <div class="text-sm text-muted-foreground mb-1">
                    General Average
                  </div>
                  <div :class="['text-3xl font-bold', getGradeColor(generalAverage)]">
                    {{ generalAverage }}%
                  </div>
                </div>
                <div class="text-center p-4 bg-background rounded-lg border">
                  <div class="text-sm text-muted-foreground mb-1">
                    Grade Point Average
                  </div>
                  <div class="text-3xl font-bold text-blue-600">{{ gpa }}</div>
                </div>
                <div class="text-center p-4 bg-background rounded-lg border">
                  <div class="text-sm text-muted-foreground mb-1">
                    Academic Standing
                  </div>
                  <div class="text-3xl font-bold text-green-600">
                    {{ generalAverage >= 90 ? 'With Honors' : 'Good Standing' }}
                  </div>
                </div>
              </div>
            </div>

            <!-- Footer Notes -->
            <div class="p-6 border-t">
              <h4 class="font-semibold mb-3">Grading System:</h4>
              <div class="grid md:grid-cols-2 gap-3 text-sm">
                <div>
                  <p class="text-muted-foreground">
                    • Written Works: 40% of Quarterly Grade
                  </p>
                  <p class="text-muted-foreground">
                    • Performance Tasks: 60% of Quarterly Grade
                  </p>
                </div>
                <div>
                  <p class="text-muted-foreground">
                    • A (90-100): Excellent | B (80-89): Good | C (75-79): Fair
                  </p>
                  <p class="text-muted-foreground">
                    • Passing Grade: 75% | GPA Scale: 1.0 - 5.0
                  </p>
                </div>
              </div>

              <div class="mt-6 pt-6 border-t flex justify-between items-center">
                <div>
                  <p class="text-sm text-muted-foreground">Generated on:</p>
                  <p class="font-semibold">February 15, 2025</p>
                </div>
                <div class="text-right">
                  <p class="text-sm text-muted-foreground">Certified by:</p>
                  <p class="font-semibold">Office of the Registrar</p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Performance Summary -->
        <Card>
          <CardHeader>
            <CardTitle>Performance Summary</CardTitle>
            <CardDescription>Quarter-by-quarter comparison</CardDescription>
          </CardHeader>
          <CardContent>
            <div class="space-y-4">
              <div class="flex items-center justify-between p-4 border rounded-lg">
                <div class="flex items-center gap-3">
                  <TrendingUp class="h-5 w-5 text-green-600" />
                  <div>
                    <p class="font-semibold">Overall Trend</p>
                    <p class="text-sm text-muted-foreground">
                      Your grades are improving this quarter
                    </p>
                  </div>
                </div>
                <Badge variant="outline" class="bg-green-50 text-green-700">
                  +2.5% from Q2
                </Badge>
              </div>

              <div class="p-4 border rounded-lg bg-blue-50">
                <p class="font-semibold text-blue-900 mb-2">Teacher's Comments:</p>
                <p class="text-sm text-blue-800">
                  Maria shows consistent improvement and dedication to her studies.
                  Her participation in class discussions is commendable. Keep up the
                  excellent work!
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>