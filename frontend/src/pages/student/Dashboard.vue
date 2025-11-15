<script lang="ts">
export const description = "Student dashboard overview"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

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
  Calendar,
  BookOpen,
  ClipboardCheck,
  Bell,
  Clock,
  Star,
  TrendingUp,
  ChevronRight,
  School,
  NotebookPen,
  GraduationCap,
} from "lucide-vue-next"

const userRole = "Student"

// Mock Student Data
const studentName = "Maria Santos"
const gradeLevel = "Grade 12 – STEM"

// Quick Stats
const quickStats = {
  attendance: "92%",
  averageGrade: "88.4%",
  completedTasks: 37,
  pendingTasks: 4,
}

// Upcoming Events
const upcomingEvents = [
  { id: 1, title: "Math Quiz", date: "Feb 18, 2025" },
  { id: 2, title: "Science Fair Practice", date: "Feb 20, 2025" },
  { id: 3, title: "School Foundation Day", date: "Mar 5, 2025" },
]

// Latest Announcements
const announcements = [
  {
    id: 1,
    title: "Submission Reminder",
    preview: "Project deadline moved to Feb 20.",
    date: "Feb 12, 2025",
  },
  {
    id: 2,
    title: "No Class Advisory",
    preview: "Holiday on Feb 25 (EDSA Celebration).",
    date: "Feb 10, 2025",
  },
  {
    id: 3,
    title: "Parent Meeting",
    preview: "Scheduled meeting on March 1.",
    date: "Feb 9, 2025",
  },
]
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
              <BreadcrumbPage>Dashboard</BreadcrumbPage>
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
        <!-- Welcome Banner -->
        <div
          class="rounded-lg border bg-gradient-to-r from-blue-100/50 via-blue-50 to-background p-6"
        >
          <div
            class="flex flex-col md:flex-row md:items-center md:justify-between gap-4"
          >
            <div>
              <h2 class="text-3xl font-bold">
                Welcome back, {{ studentName }}!
              </h2>
              <p class="text-muted-foreground mt-2">
                {{ gradeLevel }} • Here's your school overview today.
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Calendar class="mr-2 h-4 w-4" />
                View Schedule
              </Button>
              <Button>
                <TrendingUp class="mr-2 h-4 w-4" />
                View Grades
              </Button>
            </div>
          </div>
        </div>

        <!-- QUICK STATS -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Attendance</CardTitle>
              <Clock class="h-4 w-4 text-blue-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ quickStats.attendance }}</div>
              <p class="text-xs text-muted-foreground mt-1">
                Your attendance rate
              </p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Average Grade</CardTitle>
              <Star class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">
                {{ quickStats.averageGrade }}
              </div>
              <p class="text-xs text-muted-foreground mt-1">
                Your current general average
              </p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">
                Completed Tasks
              </CardTitle>
              <ClipboardCheck class="h-4 w-4 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">
                {{ quickStats.completedTasks }}
              </div>
              <p class="text-xs text-muted-foreground mt-1">
                Done this quarter
              </p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-orange-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Pending Tasks</CardTitle>
              <NotebookPen class="h-4 w-4 text-orange-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">
                {{ quickStats.pendingTasks }}
              </div>
              <p class="text-xs text-muted-foreground mt-1">
                To complete this week
              </p>
            </CardContent>
          </Card>
        </div>

        <!-- CONTENT GRID -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
          <!-- LEFT: ANNOUNCEMENTS -->
          <Card class="col-span-4">
            <CardHeader class="flex flex-row items-center justify-between">
              <div>
                <CardTitle>Latest Announcements</CardTitle>
                <CardDescription>
                  Updates from your teachers & school.
                </CardDescription>
              </div>
              <Button variant="ghost" size="sm">View All</Button>
            </CardHeader>

            <CardContent>
              <div class="space-y-3">
                <div
                  v-for="a in announcements"
                  :key="a.id"
                  class="p-4 border rounded-lg hover:bg-muted/50 cursor-pointer flex justify-between group"
                >
                  <div>
                    <p class="font-semibold">{{ a.title }}</p>
                    <p class="text-sm text-muted-foreground">
                      {{ a.preview }}
                    </p>
                    <p class="text-xs text-muted-foreground mt-1">
                      {{ a.date }}
                    </p>
                  </div>

                  <ChevronRight
                    class="opacity-0 group-hover:opacity-100 transition h-4 w-4 mt-2"
                  />
                </div>
              </div>
            </CardContent>
          </Card>

          <!-- RIGHT: UPCOMING EVENTS -->
          <Card class="col-span-3">
            <CardHeader>
              <CardTitle>Upcoming Events</CardTitle>
              <CardDescription>Your schedule this month</CardDescription>
            </CardHeader>

            <CardContent>
              <div class="space-y-3">
                <div
                  v-for="e in upcomingEvents"
                  :key="e.id"
                  class="p-3 border rounded-lg flex items-center gap-4 hover:bg-muted/50 cursor-pointer"
                >
                  <div
                    class="flex h-12 w-12 flex-col items-center justify-center bg-primary/10 text-primary rounded-lg"
                  >
                    <span class="text-xs">{{ e.date.split(" ")[0] }}</span>
                    <span class="font-bold text-lg">{{
                      e.date.split(" ")[1]
                    }}</span>
                  </div>

                  <div>
                    <p class="font-medium">{{ e.title }}</p>
                    <p class="text-xs text-muted-foreground">{{ e.date }}</p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
