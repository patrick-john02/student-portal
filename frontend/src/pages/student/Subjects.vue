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
  BookOpen,
  Bell,
  Clock,
  FileText,
  TrendingUp,
  ChevronRight,
  Calculator,
  Beaker,
  Globe,
  Languages,
  Dumbbell,
} from "lucide-vue-next"

const userRole = "Student"

// Mock Subjects Data
const subjects = [
  {
    id: 1,
    name: "Mathematics",
    teacher: "Mr. Juan dela Cruz",
    icon: "Calculator",
    color: "blue",
    grade: "90%",
    attendance: "95%",
    pendingTasks: 2,
    nextClass: "Mon, 8:00 AM",
  },
  {
    id: 2,
    name: "Science",
    teacher: "Ms. Ana Reyes",
    icon: "Beaker",
    color: "green",
    grade: "88%",
    attendance: "92%",
    pendingTasks: 1,
    nextClass: "Tue, 10:00 AM",
  },
  {
    id: 3,
    name: "English",
    teacher: "Mrs. Sofia Garcia",
    icon: "BookOpen",
    color: "purple",
    grade: "92%",
    attendance: "98%",
    pendingTasks: 0,
    nextClass: "Wed, 9:00 AM",
  },
  {
    id: 4,
    name: "Filipino",
    teacher: "Mr. Pedro Santos",
    icon: "Languages",
    color: "red",
    grade: "85%",
    attendance: "90%",
    pendingTasks: 3,
    nextClass: "Thu, 1:00 PM",
  },
  {
    id: 5,
    name: "Social Studies",
    teacher: "Ms. Maria Lopez",
    icon: "Globe",
    color: "orange",
    grade: "87%",
    attendance: "93%",
    pendingTasks: 1,
    nextClass: "Fri, 11:00 AM",
  },
  {
    id: 6,
    name: "Physical Education",
    teacher: "Coach Mike Tan",
    icon: "Dumbbell",
    color: "yellow",
    grade: "94%",
    attendance: "96%",
    pendingTasks: 0,
    nextClass: "Fri, 3:00 PM",
  },
]

const getIcon = (iconName: string) => {
  const icons: Record<string, any> = {
    Calculator,
    Beaker,
    BookOpen,
    Languages,
    Globe,
    Dumbbell,
  }
  return icons[iconName]
}

const getColorClasses = (color: string) => {
  const colors: Record<string, { border: string; bg: string; text: string }> = {
    blue: {
      border: "border-l-blue-500",
      bg: "bg-blue-500/10",
      text: "text-blue-500",
    },
    green: {
      border: "border-l-green-500",
      bg: "bg-green-500/10",
      text: "text-green-500",
    },
    purple: {
      border: "border-l-purple-500",
      bg: "bg-purple-500/10",
      text: "text-purple-500",
    },
    red: {
      border: "border-l-red-500",
      bg: "bg-red-500/10",
      text: "text-red-500",
    },
    orange: {
      border: "border-l-orange-500",
      bg: "bg-orange-500/10",
      text: "text-orange-500",
    },
    yellow: {
      border: "border-l-yellow-500",
      bg: "bg-yellow-500/10",
      text: "text-yellow-500",
    },
  }
  return colors[color] || colors.blue
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
              <BreadcrumbPage>Subjects</BreadcrumbPage>
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
          <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div>
              <h2 class="text-3xl font-bold">My Subjects</h2>
              <p class="text-muted-foreground mt-2">
                Grade 12 – STEM • 6 Subjects Enrolled
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Clock class="mr-2 h-4 w-4" />
                Class Schedule
              </Button>
              <Button>
                <TrendingUp class="mr-2 h-4 w-4" />
                View All Grades
              </Button>
            </div>
          </div>
        </div>

        <!-- SUBJECTS GRID -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          <Card
            v-for="subject in subjects"
            :key="subject.id"
            :class="['hover:shadow-lg transition-shadow cursor-pointer', getColorClasses(subject.color).border]"
          >
            <CardHeader>
              <div class="flex items-start justify-between">
                <div :class="['p-3 rounded-lg', getColorClasses(subject.color).bg]">
                  <component
                    :is="getIcon(subject.icon)"
                    :class="['h-6 w-6', getColorClasses(subject.color).text]"
                  />
                </div>
                <Badge v-if="subject.pendingTasks > 0" variant="secondary">
                  {{ subject.pendingTasks }} pending
                </Badge>
                <Badge v-else variant="outline" class="text-green-600">
                  Up to date
                </Badge>
              </div>

              <CardTitle class="mt-4">{{ subject.name }}</CardTitle>
              <CardDescription>{{ subject.teacher }}</CardDescription>
            </CardHeader>

            <CardContent>
              <div class="space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-sm text-muted-foreground">Current Grade</span>
                  <span class="font-semibold">{{ subject.grade }}</span>
                </div>

                <div class="flex justify-between items-center">
                  <span class="text-sm text-muted-foreground">Attendance</span>
                  <span class="font-semibold">{{ subject.attendance }}</span>
                </div>

                <Separator />

                <div class="flex items-center gap-2 text-sm text-muted-foreground">
                  <Clock class="h-4 w-4" />
                  <span>Next: {{ subject.nextClass }}</span>
                </div>

                <div class="flex gap-2 mt-4">
                  <Button variant="outline" size="sm" class="flex-1">
                    <FileText class="mr-2 h-4 w-4" />
                    Materials
                  </Button>
                  <Button size="sm" class="flex-1">
                    <ChevronRight class="mr-2 h-4 w-4" />
                    View Details
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>