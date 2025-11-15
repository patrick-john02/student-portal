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
  CheckCircle,
  FileText,
  Calendar,
  Eye,
  Filter,
  Search,
  Download,
  TrendingUp,
  Award,
  BarChart3,
} from "lucide-vue-next"

const userRole = "Student"

// Mock Graded Assignments Data
const gradedAssignments = [
  {
    id: 1,
    title: "Geometry Problem Set",
    subject: "Mathematics",
    teacher: "Mr. Juan dela Cruz",
    submittedDate: "Feb 5, 2025",
    gradedDate: "Feb 7, 2025",
    grade: "100/100",
    percentage: 100,
    type: "Problem Set",
    feedback: "Perfect score! Excellent work on all problems.",
  },
  {
    id: 2,
    title: "Chemical Reactions Lab Report",
    subject: "Science",
    teacher: "Ms. Ana Reyes",
    submittedDate: "Feb 10, 2025",
    gradedDate: "Feb 12, 2025",
    grade: "95/100",
    percentage: 95,
    type: "Lab Report",
    feedback: "Excellent analysis and clear presentation of results.",
  },
  {
    id: 3,
    title: "Algebraic Expressions Worksheet",
    subject: "Mathematics",
    teacher: "Mr. Juan dela Cruz",
    submittedDate: "Feb 8, 2025",
    gradedDate: "Feb 10, 2025",
    grade: "88/100",
    percentage: 88,
    type: "Worksheet",
    feedback: "Good work. Review problems 15-18 for improvement.",
  },
  {
    id: 4,
    title: "Shakespeare Analysis Essay",
    subject: "English",
    teacher: "Mrs. Sofia Garcia",
    submittedDate: "Feb 12, 2025",
    gradedDate: "Feb 14, 2025",
    grade: "82/100",
    percentage: 82,
    type: "Essay",
    feedback: "Good insights but needs better structure. Work on thesis statements.",
  },
  {
    id: 5,
    title: "Cell Structure Diagram",
    subject: "Science",
    teacher: "Ms. Ana Reyes",
    submittedDate: "Feb 3, 2025",
    gradedDate: "Feb 5, 2025",
    grade: "92/100",
    percentage: 92,
    type: "Project",
    feedback: "Very detailed and accurate labeling. Great work!",
  },
  {
    id: 6,
    title: "Rizal Biography Report",
    subject: "Filipino",
    teacher: "Mr. Pedro Santos",
    submittedDate: "Feb 1, 2025",
    gradedDate: "Feb 3, 2025",
    grade: "85/100",
    percentage: 85,
    type: "Report",
    feedback: "Good historical context. Add more primary sources next time.",
  },
  {
    id: 7,
    title: "Trigonometry Quiz",
    subject: "Mathematics",
    teacher: "Mr. Juan dela Cruz",
    submittedDate: "Jan 30, 2025",
    gradedDate: "Feb 1, 2025",
    grade: "78/100",
    percentage: 78,
    type: "Quiz",
    feedback: "Review sine and cosine laws. See me for extra help.",
  },
  {
    id: 8,
    title: "Poetry Analysis - Haiku",
    subject: "English",
    teacher: "Mrs. Sofia Garcia",
    submittedDate: "Jan 28, 2025",
    gradedDate: "Jan 30, 2025",
    grade: "90/100",
    percentage: 90,
    type: "Essay",
    feedback: "Thoughtful interpretation. Well-structured analysis.",
  },
]

// Calculate statistics
const averageGrade = Math.round(
  gradedAssignments.reduce((sum, a) => sum + a.percentage, 0) /
    gradedAssignments.length
)
const highestGrade = Math.max(...gradedAssignments.map((a) => a.percentage))
const lowestGrade = Math.min(...gradedAssignments.map((a) => a.percentage))
const excellentCount = gradedAssignments.filter((a) => a.percentage >= 90).length

const getGradeColor = (percentage: number) => {
  if (percentage >= 90) return "text-green-600"
  if (percentage >= 80) return "text-blue-600"
  if (percentage >= 75) return "text-yellow-600"
  return "text-red-600"
}

const getGradeBadge = (percentage: number) => {
  if (percentage >= 90) return { variant: "default" as const, label: "Excellent", class: "bg-green-500" }
  if (percentage >= 80) return { variant: "default" as const, label: "Good", class: "bg-blue-500" }
  if (percentage >= 75) return { variant: "secondary" as const, label: "Fair", class: "bg-yellow-500" }
  return { variant: "destructive" as const, label: "Needs Improvement", class: "bg-red-500" }
}

const getSubjectColor = (subject: string) => {
  const colors: Record<string, string> = {
    Mathematics: "text-blue-600 bg-blue-50",
    Science: "text-green-600 bg-green-50",
    English: "text-purple-600 bg-purple-50",
    Filipino: "text-red-600 bg-red-50",
    "Social Studies": "text-orange-600 bg-orange-50",
  }
  return colors[subject] || "text-gray-600 bg-gray-50"
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
              <BreadcrumbLink href="/student/assignments/pending">
                Assignments
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>Graded</BreadcrumbPage>
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
              <h2 class="text-3xl font-bold">Graded Assignments</h2>
              <p class="text-muted-foreground mt-2">
                {{ gradedAssignments.length }} assignments have been graded
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Filter class="mr-2 h-4 w-4" />
                Filter
              </Button>
              <Button variant="outline">
                <BarChart3 class="mr-2 h-4 w-4" />
                View Analytics
              </Button>
            </div>
          </div>
        </div>

        <!-- Grade Statistics -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Average Grade</CardTitle>
              <TrendingUp class="h-4 w-4 text-blue-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ averageGrade }}%</div>
              <p class="text-xs text-muted-foreground mt-1">
                Across all assignments
              </p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Highest Grade</CardTitle>
              <Award class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ highestGrade }}%</div>
              <p class="text-xs text-muted-foreground mt-1">Your best score</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Lowest Grade</CardTitle>
              <BarChart3 class="h-4 w-4 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ lowestGrade }}%</div>
              <p class="text-xs text-muted-foreground mt-1">
                Area for improvement
              </p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-purple-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Excellent Grades</CardTitle>
              <CheckCircle class="h-4 w-4 text-purple-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ excellentCount }}</div>
              <p class="text-xs text-muted-foreground mt-1">90% and above</p>
            </CardContent>
          </Card>
        </div>

        <!-- Search Bar -->
        <Card>
          <CardContent class="p-4">
            <div class="relative">
              <Search
                class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-muted-foreground"
              />
              <input
                type="text"
                placeholder="Search graded assignments..."
                class="w-full pl-10 pr-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
              />
            </div>
          </CardContent>
        </Card>

        <!-- Assignments List -->
        <div class="space-y-4">
          <Card
            v-for="assignment in gradedAssignments"
            :key="assignment.id"
            class="hover:shadow-lg transition-shadow"
          >
            <CardHeader>
              <div class="flex items-start justify-between gap-4">
                <div class="flex-1">
                  <div class="flex items-center gap-2 mb-2">
                    <Badge :class="getSubjectColor(assignment.subject)">
                      {{ assignment.subject }}
                    </Badge>
                    <Badge :variant="getGradeBadge(assignment.percentage).variant">
                      {{ getGradeBadge(assignment.percentage).label }}
                    </Badge>
                    <Badge variant="outline">{{ assignment.type }}</Badge>
                  </div>
                  <CardTitle class="text-xl">{{ assignment.title }}</CardTitle>
                  <CardDescription class="mt-2">
                    Teacher: {{ assignment.teacher }}
                  </CardDescription>
                </div>

                <div class="text-right">
                  <div
                    :class="[
                      'text-3xl font-bold',
                      getGradeColor(assignment.percentage),
                    ]"
                  >
                    {{ assignment.grade }}
                  </div>
                  <div class="text-xs text-muted-foreground mt-1">
                    {{ assignment.percentage }}%
                  </div>
                </div>
              </div>
            </CardHeader>

            <CardContent>
              <div class="space-y-4">
                <div class="flex flex-wrap gap-4 text-sm text-muted-foreground">
                  <div class="flex items-center gap-2">
                    <Calendar class="h-4 w-4" />
                    <span>Submitted: {{ assignment.submittedDate }}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <CheckCircle class="h-4 w-4" />
                    <span>Graded: {{ assignment.gradedDate }}</span>
                  </div>
                </div>

                <div class="p-4 bg-muted/50 rounded-lg border">
                  <p class="text-sm font-semibold mb-2">Teacher's Feedback:</p>
                  <p class="text-sm text-muted-foreground">
                    {{ assignment.feedback }}
                  </p>
                </div>

                <div class="flex gap-2">
                  <Button variant="outline" size="sm">
                    <Eye class="mr-2 h-4 w-4" />
                    View Submission
                  </Button>
                  <Button variant="outline" size="sm">
                    <FileText class="mr-2 h-4 w-4" />
                    View Rubric
                  </Button>
                  <Button variant="outline" size="sm">
                    <Download class="mr-2 h-4 w-4" />
                    Download
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <!-- Empty State (Hidden when there are assignments) -->
        <Card v-if="gradedAssignments.length === 0" class="p-12">
          <div class="text-center">
            <FileText class="h-16 w-16 text-muted-foreground mx-auto mb-4" />
            <h3 class="text-xl font-semibold mb-2">No Graded Assignments</h3>
            <p class="text-muted-foreground">
              You don't have any graded assignments yet.
            </p>
          </div>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>