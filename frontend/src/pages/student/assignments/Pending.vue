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
  Clock,
  FileText,
  AlertCircle,
  Calendar,
  Upload,
  Eye,
  Filter,
  Search,
} from "lucide-vue-next"

const userRole = "Student"

// Mock Pending Assignments Data
const pendingAssignments = [
  {
    id: 1,
    title: "Quadratic Equations Problem Set",
    subject: "Mathematics",
    teacher: "Mr. Juan dela Cruz",
    dueDate: "Feb 18, 2025",
    daysLeft: 3,
    priority: "high",
    type: "Problem Set",
    description: "Solve problems 1-20 on page 145",
    points: 50,
  },
  {
    id: 2,
    title: "Photosynthesis Lab Report",
    subject: "Science",
    teacher: "Ms. Ana Reyes",
    dueDate: "Feb 20, 2025",
    daysLeft: 5,
    priority: "medium",
    type: "Lab Report",
    description: "Complete analysis and conclusion sections",
    points: 100,
  },
  {
    id: 3,
    title: "Book Review - Noli Me Tangere",
    subject: "Filipino",
    teacher: "Mr. Pedro Santos",
    dueDate: "Feb 22, 2025",
    daysLeft: 7,
    priority: "medium",
    type: "Essay",
    description: "Write a 500-word critical review",
    points: 75,
  },
  {
    id: 4,
    title: "Essay: Climate Change Impact",
    subject: "English",
    teacher: "Mrs. Sofia Garcia",
    dueDate: "Feb 17, 2025",
    daysLeft: 2,
    priority: "high",
    type: "Essay",
    description: "5-paragraph argumentative essay",
    points: 80,
  },
  {
    id: 5,
    title: "Philippine History Timeline",
    subject: "Social Studies",
    teacher: "Ms. Maria Lopez",
    dueDate: "Feb 25, 2025",
    daysLeft: 10,
    priority: "low",
    type: "Project",
    description: "Create an illustrated timeline 1898-1946",
    points: 60,
  },
]

const getPriorityBadge = (priority: string, daysLeft: number) => {
  if (daysLeft <= 2) {
    return { variant: "destructive" as const, label: "Due Soon", class: "bg-red-500" }
  } else if (priority === "high") {
    return { variant: "destructive" as const, label: "High Priority", class: "bg-orange-500" }
  } else if (priority === "medium") {
    return { variant: "secondary" as const, label: "Medium", class: "bg-yellow-500" }
  } else {
    return { variant: "outline" as const, label: "Low Priority", class: "bg-gray-500" }
  }
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
              <BreadcrumbPage>Pending</BreadcrumbPage>
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
              <h2 class="text-3xl font-bold">Pending Assignments</h2>
              <p class="text-muted-foreground mt-2">
                You have {{ pendingAssignments.length }} assignments to complete
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Filter class="mr-2 h-4 w-4" />
                Filter
              </Button>
              <Button variant="outline">
                <Calendar class="mr-2 h-4 w-4" />
                Sort by Date
              </Button>
            </div>
          </div>
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
                placeholder="Search assignments..."
                class="w-full pl-10 pr-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
              />
            </div>
          </CardContent>
        </Card>

        <!-- Assignments List -->
        <div class="space-y-4">
          <Card
            v-for="assignment in pendingAssignments"
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
                    <Badge
                      :variant="getPriorityBadge(assignment.priority, assignment.daysLeft).variant"
                    >
                      {{ getPriorityBadge(assignment.priority, assignment.daysLeft).label }}
                    </Badge>
                    <Badge variant="outline">{{ assignment.type }}</Badge>
                  </div>
                  <CardTitle class="text-xl">{{ assignment.title }}</CardTitle>
                  <CardDescription class="mt-2">
                    {{ assignment.description }}
                  </CardDescription>
                </div>

                <div class="text-right">
                  <div class="text-2xl font-bold text-primary">
                    {{ assignment.points }}
                  </div>
                  <div class="text-xs text-muted-foreground">points</div>
                </div>
              </div>
            </CardHeader>

            <CardContent>
              <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div class="flex flex-wrap gap-4 text-sm text-muted-foreground">
                  <div class="flex items-center gap-2">
                    <Clock class="h-4 w-4" />
                    <span>
                      Due: {{ assignment.dueDate }} ({{ assignment.daysLeft }} days left)
                    </span>
                  </div>
                  <div class="flex items-center gap-2">
                    <FileText class="h-4 w-4" />
                    <span>{{ assignment.teacher }}</span>
                  </div>
                </div>

                <div class="flex gap-2">
                  <Button variant="outline" size="sm">
                    <Eye class="mr-2 h-4 w-4" />
                    View Details
                  </Button>
                  <Button size="sm">
                    <Upload class="mr-2 h-4 w-4" />
                    Submit Work
                  </Button>
                </div>
              </div>

              <div
                v-if="assignment.daysLeft <= 2"
                class="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg flex items-start gap-2"
              >
                <AlertCircle class="h-5 w-5 text-red-600 mt-0.5" />
                <div class="text-sm text-red-800">
                  <strong>Urgent:</strong> This assignment is due in
                  {{ assignment.daysLeft }} day(s). Please submit as soon as possible.
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <!-- Empty State (Hidden when there are assignments) -->
        <Card v-if="pendingAssignments.length === 0" class="p-12">
          <div class="text-center">
            <FileText class="h-16 w-16 text-muted-foreground mx-auto mb-4" />
            <h3 class="text-xl font-semibold mb-2">No Pending Assignments</h3>
            <p class="text-muted-foreground">
              Great job! You've completed all your assignments.
            </p>
          </div>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>