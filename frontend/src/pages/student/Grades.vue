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
  TrendingUp,
  TrendingDown,
  Award,
  FileText,
  Download,
  Calendar,
  ChevronRight,
} from "lucide-vue-next"

const userRole = "Student"

// Mock Grades Data
const subjects = [
  {
    id: 1,
    name: "Mathematics",
    teacher: "Mr. Juan dela Cruz",
    currentGrade: 90,
    previousGrade: 88,
    trend: "up",
    letterGrade: "A",
    credits: 4,
    quarters: [
      { quarter: "Q1", grade: 92 },
      { quarter: "Q2", grade: 88 },
      { quarter: "Q3", grade: 90 },
      { quarter: "Q4", grade: null },
    ],
  },
  {
    id: 2,
    name: "Science",
    teacher: "Ms. Ana Reyes",
    currentGrade: 88,
    previousGrade: 90,
    trend: "down",
    letterGrade: "B+",
    credits: 4,
    quarters: [
      { quarter: "Q1", grade: 90 },
      { quarter: "Q2", grade: 91 },
      { quarter: "Q3", grade: 88 },
      { quarter: "Q4", grade: null },
    ],
  },
  {
    id: 3,
    name: "English",
    teacher: "Mrs. Sofia Garcia",
    currentGrade: 92,
    previousGrade: 91,
    trend: "up",
    letterGrade: "A",
    credits: 4,
    quarters: [
      { quarter: "Q1", grade: 91 },
      { quarter: "Q2", grade: 90 },
      { quarter: "Q3", grade: 92 },
      { quarter: "Q4", grade: null },
    ],
  },
  {
    id: 4,
    name: "Filipino",
    teacher: "Mr. Pedro Santos",
    currentGrade: 85,
    previousGrade: 85,
    trend: "stable",
    letterGrade: "B",
    credits: 4,
    quarters: [
      { quarter: "Q1", grade: 86 },
      { quarter: "Q2", grade: 84 },
      { quarter: "Q3", grade: 85 },
      { quarter: "Q4", grade: null },
    ],
  },
  {
    id: 5,
    name: "Social Studies",
    teacher: "Ms. Maria Lopez",
    currentGrade: 87,
    previousGrade: 86,
    trend: "up",
    letterGrade: "B+",
    credits: 3,
    quarters: [
      { quarter: "Q1", grade: 85 },
      { quarter: "Q2", grade: 86 },
      { quarter: "Q3", grade: 87 },
      { quarter: "Q4", grade: null },
    ],
  },
  {
    id: 6,
    name: "Physical Education",
    teacher: "Coach Mike Tan",
    currentGrade: 94,
    previousGrade: 93,
    trend: "up",
    letterGrade: "A",
    credits: 2,
    quarters: [
      { quarter: "Q1", grade: 93 },
      { quarter: "Q2", grade: 94 },
      { quarter: "Q3", grade: 94 },
      { quarter: "Q4", grade: null },
    ],
  },
]

// Calculate GPA
const totalPoints = subjects.reduce((sum, s) => sum + s.currentGrade * s.credits, 0)
const totalCredits = subjects.reduce((sum, s) => sum + s.credits, 0)
const gpa = (totalPoints / totalCredits / 25).toFixed(2)
const overallAverage = Math.round(
  subjects.reduce((sum, s) => sum + s.currentGrade, 0) / subjects.length
)

const getGradeColor = (grade: number) => {
  if (grade >= 90) return "text-green-600"
  if (grade >= 80) return "text-blue-600"
  if (grade >= 75) return "text-yellow-600"
  return "text-red-600"
}

const getGradeBgColor = (grade: number) => {
  if (grade >= 90) return "bg-green-50 border-green-200"
  if (grade >= 80) return "bg-blue-50 border-blue-200"
  if (grade >= 75) return "bg-yellow-50 border-yellow-200"
  return "bg-red-50 border-red-200"
}

const getTrendIcon = (trend: string) => {
  if (trend === "up") return TrendingUp
  if (trend === "down") return TrendingDown
  return null
}

const getTrendColor = (trend: string) => {
  if (trend === "up") return "text-green-600"
  if (trend === "down") return "text-red-600"
  return "text-gray-600"
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
            <BreadcrumbItem>
              <BreadcrumbPage>Grades</BreadcrumbPage>
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
        <div class="rounded-lg border bg-gradient-to-r from-blue-50 to-background p-6">
          <div
            class="flex flex-col md:flex-row md:items-center md:justify-between gap-4"
          >
            <div>
              <h2 class="text-3xl font-bold">Grade Report</h2>
              <p class="text-muted-foreground mt-2">
                Grade 12 – STEM • Quarter 3, Academic Year 2024-2025
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Calendar class="mr-2 h-4 w-4" />
                Select Quarter
              </Button>
              <Button>
                <Download class="mr-2 h-4 w-4" />
                Download Report
              </Button>
            </div>
          </div>
        </div>

        <!-- Overall Statistics -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Overall Average</CardTitle>
              <Award class="h-4 w-4 text-blue-500" />
            </CardHeader>
            <CardContent>
              <div class="text-3xl font-bold">{{ overallAverage }}%</div>
              <p class="text-xs text-muted-foreground mt-1">
                Across all subjects
              </p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">GPA</CardTitle>
              <TrendingUp class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-3xl font-bold">{{ gpa }}</div>
              <p class="text-xs text-muted-foreground mt-1">Grade Point Average</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-purple-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Total Credits</CardTitle>
              <FileText class="h-4 w-4 text-purple-500" />
            </CardHeader>
            <CardContent>
              <div class="text-3xl font-bold">{{ totalCredits }}</div>
              <p class="text-xs text-muted-foreground mt-1">This quarter</p>
            </CardContent>
          </Card>
        </div>

        <!-- Subjects Grades -->
        <Card>
          <CardHeader>
            <CardTitle>Subject Grades</CardTitle>
            <CardDescription>
              Current quarter grades and performance trends
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div class="space-y-4">
              <div
                v-for="subject in subjects"
                :key="subject.id"
                class="p-4 border rounded-lg hover:shadow-md transition-shadow cursor-pointer"
              >
                <div class="flex items-start justify-between gap-4">
                  <div class="flex-1">
                    <div class="flex items-center gap-3 mb-2">
                      <h3 class="font-semibold text-lg">{{ subject.name }}</h3>
                      <Badge
                        :class="getGradeBgColor(subject.currentGrade)"
                        class="border"
                      >
                        {{ subject.letterGrade }}
                      </Badge>
                      <Badge variant="outline" class="text-xs">
                        {{ subject.credits }} credits
                      </Badge>
                    </div>
                    <p class="text-sm text-muted-foreground">
                      {{ subject.teacher }}
                    </p>

                    <!-- Quarterly Grades -->
                    <div class="flex gap-4 mt-3">
                      <div
                        v-for="q in subject.quarters"
                        :key="q.quarter"
                        class="text-center"
                      >
                        <div class="text-xs text-muted-foreground mb-1">
                          {{ q.quarter }}
                        </div>
                        <div
                          v-if="q.grade"
                          :class="[
                            'text-sm font-semibold px-2 py-1 rounded',
                            getGradeBgColor(q.grade),
                          ]"
                        >
                          {{ q.grade }}%
                        </div>
                        <div
                          v-else
                          class="text-sm text-muted-foreground px-2 py-1"
                        >
                          —
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="text-right">
                    <div
                      :class="['text-3xl font-bold', getGradeColor(subject.currentGrade)]"
                    >
                      {{ subject.currentGrade }}%
                    </div>
                    <div
                      v-if="getTrendIcon(subject.trend)"
                      :class="['flex items-center justify-end gap-1 text-sm mt-1', getTrendColor(subject.trend)]"
                    >
                      <component :is="getTrendIcon(subject.trend)" class="h-4 w-4" />
                      <span>
                        {{ Math.abs(subject.currentGrade - subject.previousGrade) }}%
                      </span>
                    </div>
                    <div v-else class="text-sm text-muted-foreground mt-1">
                      Stable
                    </div>
                  </div>
                </div>

                <div class="flex justify-end mt-4">
                  <Button variant="ghost" size="sm">
                    View Details
                    <ChevronRight class="ml-2 h-4 w-4" />
                  </Button>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Grading Scale -->
        <Card>
          <CardHeader>
            <CardTitle class="text-base">Grading Scale</CardTitle>
          </CardHeader>
          <CardContent>
            <div class="grid grid-cols-2 md:grid-cols-5 gap-3">
              <div class="p-3 bg-green-50 border border-green-200 rounded-lg">
                <div class="font-semibold text-green-700">A (90-100)</div>
                <div class="text-xs text-muted-foreground">Excellent</div>
              </div>
              <div class="p-3 bg-blue-50 border border-blue-200 rounded-lg">
                <div class="font-semibold text-blue-700">B (80-89)</div>
                <div class="text-xs text-muted-foreground">Good</div>
              </div>
              <div class="p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
                <div class="font-semibold text-yellow-700">C (75-79)</div>
                <div class="text-xs text-muted-foreground">Fair</div>
              </div>
              <div class="p-3 bg-orange-50 border border-orange-200 rounded-lg">
                <div class="font-semibold text-orange-700">D (70-74)</div>
                <div class="text-xs text-muted-foreground">Passing</div>
              </div>
              <div class="p-3 bg-red-50 border border-red-200 rounded-lg">
                <div class="font-semibold text-red-700">F (Below 70)</div>
                <div class="text-xs text-muted-foreground">Failing</div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>