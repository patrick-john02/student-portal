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
  XCircle,
  Clock,
  Calendar,
  Download,
  ChevronLeft,
  ChevronRight,
  AlertTriangle,
} from "lucide-vue-next"

const userRole = "Student"

// Current month and year
const currentMonth = "February 2025"

// Attendance Statistics
const stats = {
  present: 18,
  absent: 1,
  late: 2,
  excused: 1,
  totalDays: 20,
  attendanceRate: 90,
}

// Calendar data for February 2025
const calendarDays = [
  { date: 1, day: "Sat", status: null }, // Weekend
  { date: 2, day: "Sun", status: null }, // Weekend
  { date: 3, day: "Mon", status: "present" },
  { date: 4, day: "Tue", status: "present" },
  { date: 5, day: "Wed", status: "present" },
  { date: 6, day: "Thu", status: "late" },
  { date: 7, day: "Fri", status: "present" },
  { date: 8, day: "Sat", status: null },
  { date: 9, day: "Sun", status: null },
  { date: 10, day: "Mon", status: "present" },
  { date: 11, day: "Tue", status: "absent" },
  { date: 12, day: "Wed", status: "present" },
  { date: 13, day: "Thu", status: "present" },
  { date: 14, day: "Fri", status: "present" },
  { date: 15, day: "Sat", status: null },
  { date: 16, day: "Sun", status: null },
  { date: 17, day: "Mon", status: "present" },
  { date: 18, day: "Tue", status: "present" },
  { date: 19, day: "Wed", status: "present" },
  { date: 20, day: "Thu", status: "late" },
  { date: 21, day: "Fri", status: "present" },
  { date: 22, day: "Sat", status: null },
  { date: 23, day: "Sun", status: null },
  { date: 24, day: "Mon", status: null }, // Future
  { date: 25, day: "Tue", status: null },
  { date: 26, day: "Wed", status: null },
  { date: 27, day: "Thu", status: null },
  { date: 28, day: "Fri", status: null },
]

// Recent Attendance Records
const recentRecords = [
  {
    date: "Feb 21, 2025",
    day: "Friday",
    timeIn: "7:45 AM",
    timeOut: "4:00 PM",
    status: "present",
    remarks: "On time",
  },
  {
    date: "Feb 20, 2025",
    day: "Thursday",
    timeIn: "8:15 AM",
    timeOut: "4:05 PM",
    status: "late",
    remarks: "Arrived 15 minutes late",
  },
  {
    date: "Feb 19, 2025",
    day: "Wednesday",
    timeIn: "7:50 AM",
    timeOut: "4:00 PM",
    status: "present",
    remarks: "On time",
  },
  {
    date: "Feb 18, 2025",
    day: "Tuesday",
    timeIn: "7:45 AM",
    timeOut: "4:00 PM",
    status: "present",
    remarks: "On time",
  },
  {
    date: "Feb 17, 2025",
    day: "Monday",
    timeIn: "7:40 AM",
    timeOut: "4:00 PM",
    status: "present",
    remarks: "On time",
  },
]

const getStatusColor = (status: string | null) => {
  if (!status) return "bg-gray-100 text-gray-400"
  const colors: Record<string, string> = {
    present: "bg-green-100 text-green-700 border-green-300",
    absent: "bg-red-100 text-red-700 border-red-300",
    late: "bg-yellow-100 text-yellow-700 border-yellow-300",
    excused: "bg-blue-100 text-blue-700 border-blue-300",
  }
  return colors[status] || "bg-gray-100 text-gray-400"
}

const getStatusBadge = (status: string) => {
  const badges: Record<string, any> = {
    present: { variant: "default", label: "Present", class: "bg-green-500" },
    absent: { variant: "destructive", label: "Absent", class: "" },
    late: { variant: "secondary", label: "Late", class: "bg-yellow-500" },
    excused: { variant: "default", label: "Excused", class: "bg-blue-500" },
  }
  return badges[status] || badges.present
}

const getStatusIcon = (status: string) => {
  const icons: Record<string, any> = {
    present: CheckCircle,
    absent: XCircle,
    late: Clock,
    excused: AlertTriangle,
  }
  return icons[status] || CheckCircle
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
              <BreadcrumbPage>Attendance</BreadcrumbPage>
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
              <h2 class="text-3xl font-bold">Attendance Record</h2>
              <p class="text-muted-foreground mt-2">
                Track your daily attendance and punctuality
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Calendar class="mr-2 h-4 w-4" />
                View History
              </Button>
              <Button>
                <Download class="mr-2 h-4 w-4" />
                Download Report
              </Button>
            </div>
          </div>
        </div>

        <!-- Attendance Statistics -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-5">
          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Present</CardTitle>
              <CheckCircle class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ stats.present }}</div>
              <p class="text-xs text-muted-foreground mt-1">days</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-red-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Absent</CardTitle>
              <XCircle class="h-4 w-4 text-red-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ stats.absent }}</div>
              <p class="text-xs text-muted-foreground mt-1">days</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Late</CardTitle>
              <Clock class="h-4 w-4 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ stats.late }}</div>
              <p class="text-xs text-muted-foreground mt-1">times</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Excused</CardTitle>
              <AlertTriangle class="h-4 w-4 text-blue-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ stats.excused }}</div>
              <p class="text-xs text-muted-foreground mt-1">days</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-purple-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Rate</CardTitle>
              <Calendar class="h-4 w-4 text-purple-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ stats.attendanceRate }}%</div>
              <p class="text-xs text-muted-foreground mt-1">attendance</p>
            </CardContent>
          </Card>
        </div>

        <!-- Calendar View -->
        <Card>
          <CardHeader>
            <div class="flex items-center justify-between">
              <div>
                <CardTitle>Monthly Calendar</CardTitle>
                <CardDescription>{{ currentMonth }}</CardDescription>
              </div>
              <div class="flex gap-2">
                <Button variant="outline" size="icon">
                  <ChevronLeft class="h-4 w-4" />
                </Button>
                <Button variant="outline" size="icon">
                  <ChevronRight class="h-4 w-4" />
                </Button>
              </div>
            </div>
          </CardHeader>
          <CardContent>
            <div class="grid grid-cols-7 gap-2">
              <!-- Day Headers -->
              <div
                v-for="day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']"
                :key="day"
                class="text-center text-sm font-semibold text-muted-foreground p-2"
              >
                {{ day }}
              </div>

              <!-- Calendar Days -->
              <div
                v-for="dayData in calendarDays"
                :key="dayData.date"
                :class="[
                  'aspect-square p-2 rounded-lg text-center border-2 cursor-pointer transition-all',
                  getStatusColor(dayData.status),
                  dayData.status ? 'hover:shadow-md' : '',
                ]"
              >
                <div class="font-semibold">{{ dayData.date }}</div>
                <div v-if="dayData.status" class="text-xs mt-1">
                  {{ dayData.status === 'present' ? '✓' : dayData.status === 'absent' ? '✗' : dayData.status === 'late' ? '⏰' : '!' }}
                </div>
              </div>
            </div>

            <!-- Legend -->
            <div class="flex flex-wrap gap-4 mt-6 pt-6 border-t">
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-green-100 border-2 border-green-300 rounded"></div>
                <span class="text-sm">Present</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-red-100 border-2 border-red-300 rounded"></div>
                <span class="text-sm">Absent</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-yellow-100 border-2 border-yellow-300 rounded"></div>
                <span class="text-sm">Late</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-blue-100 border-2 border-blue-300 rounded"></div>
                <span class="text-sm">Excused</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 bg-gray-100 border-2 border-gray-200 rounded"></div>
                <span class="text-sm">Weekend/Holiday</span>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Recent Attendance Records -->
        <Card>
          <CardHeader>
            <CardTitle>Recent Records</CardTitle>
            <CardDescription>Your latest attendance entries</CardDescription>
          </CardHeader>
          <CardContent>
            <div class="space-y-3">
              <div
                v-for="(record, index) in recentRecords"
                :key="index"
                class="p-4 border rounded-lg hover:shadow-md transition-shadow"
              >
                <div class="flex items-center justify-between gap-4">
                  <div class="flex items-center gap-4 flex-1">
                    <div
                      :class="[
                        'p-3 rounded-lg',
                        record.status === 'present' ? 'bg-green-50' : 
                        record.status === 'late' ? 'bg-yellow-50' : 
                        record.status === 'absent' ? 'bg-red-50' : 'bg-blue-50'
                      ]"
                    >
                      <component
                        :is="getStatusIcon(record.status)"
                        :class="[
                          'h-5 w-5',
                          record.status === 'present' ? 'text-green-600' : 
                          record.status === 'late' ? 'text-yellow-600' : 
                          record.status === 'absent' ? 'text-red-600' : 'text-blue-600'
                        ]"
                      />
                    </div>

                    <div class="flex-1">
                      <div class="flex items-center gap-2 mb-1">
                        <p class="font-semibold">{{ record.date }}</p>
                        <Badge :variant="getStatusBadge(record.status).variant">
                          {{ getStatusBadge(record.status).label }}
                        </Badge>
                      </div>
                      <p class="text-sm text-muted-foreground">
                        {{ record.day }}
                      </p>
                    </div>

                    <div class="text-right">
                      <div class="text-sm font-medium">
                        {{ record.timeIn }} - {{ record.timeOut }}
                      </div>
                      <div class="text-xs text-muted-foreground mt-1">
                        {{ record.remarks }}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Attendance Alert -->
        <Card
          v-if="stats.attendanceRate < 95"
          class="bg-yellow-50 border-yellow-200"
        >
          <CardContent class="p-6">
            <div class="flex items-start gap-4">
              <AlertTriangle class="h-6 w-6 text-yellow-600 mt-0.5" />
              <div>
                <h3 class="font-bold text-yellow-900">Attendance Notice</h3>
                <p class="text-sm text-yellow-800 mt-1">
                  Your attendance rate is below 95%. Please maintain regular
                  attendance to ensure academic success. If you have any concerns,
                  please contact the school office.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>