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
  Calendar,
  Clock,
  Download,
  MapPin,
  ChevronLeft,
  ChevronRight,
} from "lucide-vue-next"

const userRole = "Student"

// Time slots
const timeSlots = [
  "7:00 AM",
  "8:00 AM",
  "9:00 AM",
  "10:00 AM",
  "11:00 AM",
  "12:00 PM",
  "1:00 PM",
  "2:00 PM",
  "3:00 PM",
  "4:00 PM",
]

// Days of the week
const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

// Mock Schedule Data
const schedule: Record<string, any[]> = {
  Monday: [
    {
      time: "8:00 AM",
      subject: "Mathematics",
      teacher: "Mr. Juan dela Cruz",
      room: "Room 301",
      color: "blue",
      duration: 2,
    },
    {
      time: "10:00 AM",
      subject: "English",
      teacher: "Mrs. Sofia Garcia",
      room: "Room 205",
      color: "purple",
      duration: 1,
    },
    {
      time: "1:00 PM",
      subject: "Physical Education",
      teacher: "Coach Mike Tan",
      room: "Gym",
      color: "yellow",
      duration: 2,
    },
  ],
  Tuesday: [
    {
      time: "7:00 AM",
      subject: "Filipino",
      teacher: "Mr. Pedro Santos",
      room: "Room 102",
      color: "red",
      duration: 1,
    },
    {
      time: "10:00 AM",
      subject: "Science",
      teacher: "Ms. Ana Reyes",
      room: "Lab 201",
      color: "green",
      duration: 2,
    },
    {
      time: "1:00 PM",
      subject: "Social Studies",
      teacher: "Ms. Maria Lopez",
      room: "Room 304",
      color: "orange",
      duration: 1,
    },
  ],
  Wednesday: [
    {
      time: "8:00 AM",
      subject: "Mathematics",
      teacher: "Mr. Juan dela Cruz",
      room: "Room 301",
      color: "blue",
      duration: 2,
    },
    {
      time: "11:00 AM",
      subject: "English",
      teacher: "Mrs. Sofia Garcia",
      room: "Room 205",
      color: "purple",
      duration: 1,
    },
    {
      time: "2:00 PM",
      subject: "Science",
      teacher: "Ms. Ana Reyes",
      room: "Lab 201",
      color: "green",
      duration: 1,
    },
  ],
  Thursday: [
    {
      time: "7:00 AM",
      subject: "Social Studies",
      teacher: "Ms. Maria Lopez",
      room: "Room 304",
      color: "orange",
      duration: 2,
    },
    {
      time: "10:00 AM",
      subject: "Filipino",
      teacher: "Mr. Pedro Santos",
      room: "Room 102",
      color: "red",
      duration: 1,
    },
    {
      time: "1:00 PM",
      subject: "Mathematics",
      teacher: "Mr. Juan dela Cruz",
      room: "Room 301",
      color: "blue",
      duration: 2,
    },
  ],
  Friday: [
    {
      time: "8:00 AM",
      subject: "English",
      teacher: "Mrs. Sofia Garcia",
      room: "Room 205",
      color: "purple",
      duration: 1,
    },
    {
      time: "10:00 AM",
      subject: "Science",
      teacher: "Ms. Ana Reyes",
      room: "Lab 201",
      color: "green",
      duration: 2,
    },
    {
      time: "3:00 PM",
      subject: "Physical Education",
      teacher: "Coach Mike Tan",
      room: "Gym",
      color: "yellow",
      duration: 1,
    },
  ],
}

const getColorClasses = (color: string) => {
  const colors: Record<string, string> = {
    blue: "bg-blue-500/10 border-l-4 border-l-blue-500 text-blue-700",
    green: "bg-green-500/10 border-l-4 border-l-green-500 text-green-700",
    purple: "bg-purple-500/10 border-l-4 border-l-purple-500 text-purple-700",
    red: "bg-red-500/10 border-l-4 border-l-red-500 text-red-700",
    orange: "bg-orange-500/10 border-l-4 border-l-orange-500 text-orange-700",
    yellow: "bg-yellow-500/10 border-l-4 border-l-yellow-500 text-yellow-700",
  }
  return colors[color] || colors.blue
}

const getClassForTimeSlot = (day: string, time: string) => {
  const daySchedule = schedule[day] || []
  return daySchedule.find((cls) => cls.time === time)
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
              <BreadcrumbPage>Schedule</BreadcrumbPage>
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
              <h2 class="text-3xl font-bold">Class Schedule</h2>
              <p class="text-muted-foreground mt-2">
                Grade 12 – STEM • Week of Feb 17-21, 2025
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline" size="icon">
                <ChevronLeft class="h-4 w-4" />
              </Button>
              <Button variant="outline">
                <Calendar class="mr-2 h-4 w-4" />
                This Week
              </Button>
              <Button variant="outline" size="icon">
                <ChevronRight class="h-4 w-4" />
              </Button>
              <Button>
                <Download class="mr-2 h-4 w-4" />
                Export
              </Button>
            </div>
          </div>
        </div>

        <!-- SCHEDULE TABLE -->
        <Card>
          <CardContent class="p-0">
            <div class="overflow-x-auto">
              <table class="w-full border-collapse">
                <thead>
                  <tr class="border-b bg-muted/50">
                    <th
                      class="p-4 text-left font-semibold text-sm w-32 sticky left-0 bg-muted/50"
                    >
                      Time
                    </th>
                    <th
                      v-for="day in days"
                      :key="day"
                      class="p-4 text-center font-semibold text-sm min-w-[200px]"
                    >
                      {{ day }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(time, index) in timeSlots"
                    :key="time"
                    :class="[
                      'border-b',
                      index % 2 === 0 ? 'bg-background' : 'bg-muted/20',
                    ]"
                  >
                    <td
                      class="p-4 text-sm font-medium text-muted-foreground sticky left-0"
                      :class="[
                        index % 2 === 0 ? 'bg-background' : 'bg-muted/20',
                      ]"
                    >
                      {{ time }}
                    </td>
                    <td
                      v-for="day in days"
                      :key="`${day}-${time}`"
                      class="p-2 align-top"
                    >
                      <div
                        v-if="getClassForTimeSlot(day, time)"
                        :class="[
                          'p-3 rounded-lg cursor-pointer hover:shadow-md transition-shadow',
                          getColorClasses(
                            getClassForTimeSlot(day, time)?.color
                          ),
                        ]"
                        :style="{
                          minHeight: `${
                            (getClassForTimeSlot(day, time)?.duration || 1) *
                            60
                          }px`,
                        }"
                      >
                        <p class="font-semibold text-sm">
                          {{ getClassForTimeSlot(day, time)?.subject }}
                        </p>
                        <p class="text-xs opacity-80 mt-1">
                          {{ getClassForTimeSlot(day, time)?.teacher }}
                        </p>
                        <div class="flex items-center gap-1 mt-2 text-xs opacity-70">
                          <MapPin class="h-3 w-3" />
                          <span>{{ getClassForTimeSlot(day, time)?.room }}</span>
                        </div>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>

        <!-- LEGEND -->
        <Card>
          <CardHeader>
            <CardTitle class="text-base">Schedule Legend</CardTitle>
          </CardHeader>
          <CardContent>
            <div class="flex flex-wrap gap-4">
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-blue-500/20 border-l-4 border-l-blue-500 rounded"></div>
                <span class="text-sm">Mathematics</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-green-500/20 border-l-4 border-l-green-500 rounded"></div>
                <span class="text-sm">Science</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-purple-500/20 border-l-4 border-l-purple-500 rounded"></div>
                <span class="text-sm">English</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-red-500/20 border-l-4 border-l-red-500 rounded"></div>
                <span class="text-sm">Filipino</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-orange-500/20 border-l-4 border-l-orange-500 rounded"></div>
                <span class="text-sm">Social Studies</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-yellow-500/20 border-l-4 border-l-yellow-500 rounded"></div>
                <span class="text-sm">Physical Education</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>